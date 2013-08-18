import logging
import datetime
import re
from liquidluck.utils import to_unicode
from liquidluck.readers.markdown import MarkdownReader


class MarkdownReader(MarkdownReader):
    def render(self):
        f = open(self.filepath)
        logging.debug('read ' + self.relative_filepath)

        header = ''
        body = ''
        recording = True
        for line in f:
            if recording and line.startswith('---'):
                recording = False
            elif recording:
                header += line
            else:
                body += line

        if not len(body):
            header = ''
            body = ''
            f.seek(0)
            recording = True
            for line in f:
                if recording and line.startswith('# '):
                    header += line
                    recording = False
                else:
                    body += line

        f.close()
        body = to_unicode(body)
        meta = self._parse_meta(header, body)
        content = self._parse_content(body)
        return self.post_class(self.filepath, content, meta=meta)

    def _parse_meta(self, header, body):
        meta = super(MarkdownReader, self)._parse_meta(header, body)

        if 'description' in meta:
            meta['description_source'] = meta['description']
            meta['description'] = self._parse_content(meta['description'])

        if 'date' not in meta:
            m = re.match('.*/(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*).md', self.filepath)
            if m:
                meta['date'] = datetime.datetime.strptime(m.group('date'), '%Y-%m-%d')
                meta['slug'] = m.group('slug')

        return meta
