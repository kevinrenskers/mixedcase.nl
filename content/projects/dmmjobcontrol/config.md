# Configuration
- template: jobcontrol.html
- submenu: config
---------------------

# Configuration
All configuration can be done using the Constant Editor. Descriptions of the available options are given there too, so there is little need to repeat them here (unless there is some demand for it in the future).

## Using your own html templates

It's pretty easy to use your own html templates for the listview, detailview, apply form or the searchform. Each view has its own template. The best way to look at how to set up your own template and which template codes are supported, is to have a look at the default templates. You can find them in the [typo3conf/ext/dmmcobcontrol/res](https://github.com/kevinrenskers/dmmjobcontrol/tree/master/res) folder on your server. If you cannot access that folder just go to this link, click on the extension title and you will see a list of all files that belong to JobControl, including the 4 templates.

Using your own template is done by either using the constant editor or setting the TypoScript code directly:

```text
plugin.tx_dmmjobcontrol_pi1.template.search = fileadmin/search.tmpl
```

## Changing a label
If you are not happy with one of the default labels, you can change them with TypoScript like this. For a list of all labels, please look in the file [pi1/locallang.xml](https://github.com/kevinrenskers/dmmjobcontrol/blob/master/pi1/locallang.xml).

```text
plugin.tx_dmmjobcontrol_pi1._LOCAL_LANG.default.location_label = Area
plugin.tx_dmmjobcontrol_pi1._LOCAL_LANG.nl.employer_label = Bedrijfsnaam
```

##Substitute page title by job title
On the detail page the page title will normally be something like "Jobs" or "Detail", depending on the title you've given the page and if you use the "Road 1" approach or not. By setting the `substitutePageTitle` option to 1 (which is the default setting) the page title will be changed to the job title, so this will be shown in the title tag.

However, this only works automatically for the title tag, if you use the title field in your TypoScript template, some extra work needs to be done. For example, in a site we show the page title as a nice image on all pages. By overwriting the title field with a registered value, it now changes to the job title in the detail view:

```text
# Page title as nice image
temp.titleTemplate = IMAGE
temp.titleTemplate {
    stdWrap.fieldRequired = title
    altText.field = title
    file = GIFBUILDER
    file {
        XY = [10.w]+6, [10.h]+3
        backColor = #F6F9F0
        10 = TEXT
        10.text.field = title
        10.text.override.data = register:JOBTITLE
        10.offset = 0,13
        10.fontFile = fileadmin/font.ttf
        10.fontSize = 16px
        10.fontColor = #696968
    }
}

# Load the above image into our HTML template
page.10.subparts.TITLE < temp.titleTemplate
```

The register value `JOBTITLE` is set in the extension and can be used anywhere within your TypoScript template. Be aware however that this is a tricky function, in the sense that it all depends on the order of content and extensions being loaded by TYPO3. If you notice that the register value doesn't work for you, try changed the order of the different subparts entries.


## TypoScript only

Including the searchform with TypoScript only to show it on all pages, and setting another html template at the same time.

```text
temp.jobsearch = TEMPLATE
temp.jobsearch < plugin.tx_dmmjobcontrol_pi1
temp.jobsearch.display = SEARCH
temp.jobsearch.template.search = fileadmin/search.tmpl
page.10.subparts.JOBSEARCH < temp.jobsearch
```


## Creating RSS feeds

You can create RSS feeds showing all (or the latest 20 for example) jobs. Create a new page, set the "General Records Storage page" option if needed, and create an extension template with the following code in the setup part:

```text
# Destroy the current page object
page >

# Create a new page object and set some basic options. All these options are important!
page = PAGE
page.typeNum = 0
page.config.baseURL = http://www.example.com/
page.config.tx_realurl_enable = 1
page.config.disableAllHeaderCode = 1
page.config.no_cache = 1
page.config.renderCharset = iso-8859-1
page.config.disableCharsetHeader = 1
page.config.xhtml_cleaning = 0

# Set JobControl options: show last 20 jobs
plugin.tx_dmmjobcontrol_pi1.display = RSS
plugin.tx_dmmjobcontrol_pi1.limit = 20
plugin.tx_dmmjobcontrol_pi1.rss.title = Recent jobs of example company
plugin.tx_dmmjobcontrol_pi1.rss.description = The 20 most recent jobs added to www.example.com
plugin.tx_dmmjobcontrol_pi1.rss.image = fileadmin/rss_logo.jpg

# Important is to correctly set the pid.detail and pid.list options to the correct pages
# Also this specific crdate_stdWrap.strftime is required for valid feeds!
plugin.tx_dmmjobcontrol_pi1.pid.list = 1
plugin.tx_dmmjobcontrol_pi1.pid.detail = 1
plugin.tx_dmmjobcontrol_pi1.crdate_stdWrap.strftime = %a, %d %b %Y %T %z

# Add JobControl to the page as the only content
page.10 < plugin.tx_dmmjobcontrol_pi1
```

If you don't want to have a logo in your RSS feed, clear the default image like this:

```text
plugin.tx_dmmjobcontrol_pi1.rss.image >
```


## Using stdWrap functions on fields and labels

Almost all fields can be given a stdWrap configuration, so you can change the looks of the content without necessarily using your own html templates. You can for example do this in your TypoScript setup:

```text
plugin.tx_dmmjobcontrol_pi1.reference_stdWrap.case = upper
plugin.tx_dmmjobcontrol_pi1.job_title_stdWrap.wrap = <div id=”functionTitle”>|</div>
plugin.tx_dmmjobcontrol_pi1.location_label_stdWrap.wrap = <b>|</b>
```

These are all the stdWrap fields and labels for you to use:

<table style="width:100%;">
    <tr>
        <td>
            <strong>Database fields</strong><br/>
            crdate_stdWrap<br/>
            tstamp_stdWrap<br/>
            reference_stdWrap<br/>
            job_title_stdWrap<br/>
            employet_stdWrap<br/>
            employer_description_stdWrap<br/>
            location_stdWrap<br/>
            short_job_description_stdWrap<br/>
            job_description_stdWrap<br/>
            experience_stdWrap<br/>
            job_requirements_stdWrap<br/>
            salary_stdWrap<br/>
            job_type_stdWrap<br/>
            contract_type_stdWrap<br/>
            region_stdWrap<br/>
            sector_stdWrap<br/>
            category_stdWrap<br/>
            discipline_stdWrap<br/>
            education_stdWrap<br/>
            job_benefits_stdWrap<br/>
            apply_information_stdWrap
        </td>
        <td style="width:50%;">
            <strong>Fields</strong><br/>
            crdate_label_stdWrap<br/>
            tstamp_label_stdWrap<br/>
            reference_label_stdWrap<br/>
            job_title_label_stdWrap<br/>
            employer_label_stdWrap<br/>
            employer_description_label_stdWrap<br/>
            location_label_stdWrap<br/>
            short_job_description_label_stdWrap<br/>
            job_description_label_stdWrap<br/>
            experience_label_stdWrap<br/>
            job_requirements_label_stdWrap<br/>
            salary_label_stdWrap<br/>
            job_type_label_stdWrap<br/>
            contract_type_label_stdWrap<br/>
            region_label_stdWrap<br/>
            sector_label_stdWrap<br/>
            category_label_stdWrap<br/>
            discipline_label_stdWrap<br/>
            education_label_stdWrap<br/>
            search_label_stdWrap<br/>
            reset_label_stdWrap<br/>
            backtolist_stdWrap<br/>
            backtojob_stdWrap<br/>
            keyword_label_stdWrap<br/>
            apply_header_stdWrap<br/>
            fullname_label_stdWrap<br/>
            email_label_stdWrap<br/>
            apply_label_stdWrap<br/>
            motivation_label_stdWrap<br/>
            cv_label_stdWrap<br/>
            apply_link_stdWrap<br/>
            apply_thanks_stdWrap<br/>
            job_benefits_label_stdWrap<br/>
            apply_information_label_stdWrap
        </td>
    </tr>
</table>

Some of the fields mentioned above have a default stdWrap configuration. This is the default setup code:

```text
plugin.tx_dmmjobcontrol_pi1 {
    general_stdWrap.parseFunc < tt_content.text.20.parseFunc
    crdate_stdWrap.strftime = %b %e, %Y
    employer_description_stdWrap < .general_stdWrap
    job_description_stdWrap < .general_stdWrap
    job_requirements_stdWrap < .general_stdWrap
    job_benefits_stdWrap < .general_stdWrap
    apply_information_stdWrap < .general_stdWrap
    salary_stdWrap < .general_stdWrap
    apply_required_stdWrap.wrap = |<span class="dmmjobcontrol_apply_required">*</span>
}
```

This makes sure all of the (RTE) textarea's are parsed through the default parse function, to make correct html. Of course you can override or remove any of these defaults in your own setup code.


## Example RealURL config

This will make nice url's like www.example.com/jobs/details/senior-webdeveloper and www.example.com/jobs/page/3 if you use the page-browser. Just copy the parts that you need...

```php
<?php
$TYPO3_CONF_VARS['EXTCONF']['realurl'] = array(
    'example.com' => array(
        'init' => array(
            'appendMissingSlash' => 'ifNotFile',
            'enableUrlDecodeCache' => 1,
            'enableUrlEncodeCache' => 1,
            'enableCHashCache' => 1,
        ),
        'pagePath' => array(
            'type' => 'user',
            'userFunc' => 'EXT:realurl/class.tx_realurl_advanced.php:&tx_realurl_advanced->main',
            'rootpage_id' => 1,
            'spaceCharacter' => '-',
            'languageGetVar' => 'L',
            'expireDays' => 3,
            'disablePathCache' => false,
        ),
        // Start pages with language selector like www.example.com/en/jobs/
        'preVars' => array(
            array(
                'GETvar' => 'L',
                'valueMap' => array(
                    'en' => '3',
                ),
                'noMatch' => 'bypass',
            ),
        ),
        // Give url's like /jobs/detail/programmer, and respect localization!
        'postVarSets' => array(
            '_DEFAULT' => array(
                'detail' => array(
                    array(
                        'GETvar' => 'tx_dmmjobcontrol_pi1[job_uid]',
                        'lookUpTable' => array(
                            'table' => 'tx_dmmjobcontrol_job',
                            'id_field' => 'uid',
                            'alias_field' => 'job_title',
                            'addWhereClause' => ' AND NOT deleted',
                            'useUniqueCache' => 1,
                            'useUniqueCache_conf' => array(
                                'strtolower' => 1,
                                'spaceCharacter' => '-',
                            ),
                            'languageGetVar' => 'L',
                            'languageExceptionUids' => '',
                            'languageField' => 'sys_language_uid',
                            'transOrigPointerField' => 'l18n_parent'
                        ),
                    ),
                ),
                // Give url's like jobs/page/3 for use with the page-browser
                'page' => array(
                    array(
                        'GETvar' => 'tx_dmmjobcontrol_pi1[page]',
                    ),
                ),
            ),
        ),
    ),
);
?>
```

If you want to use the language selector in the url as used in the RealURL example given here (to get url's like www.example.com/en/jobs/), put this at the very end in your TypoScript setup code:

```text
# Setting up the language variable "L" to be passed along with links .
# We map English to uid 3, but you could use anything really...
# Just make sure you map it to the same value in your RealURL config.
config.linkVars = L

[globalVar = GP:L = 3]
config.sys_language_uid = 3
config.language = en

[global]
```


## Example CoolURI config
```text
<uriparts>
    <!--[...]-->
        <part>
            <parameter>tx_dmmjobcontrol_pi1[job_uid]</parameter>
            <lookindb>
                <to>SELECT job_title FROM tx_dmmjobcontrol_job WHERE uid=$1</to>
                <translatetoif>
                    <match>^[0-9]+$</match>
                </translatetoif>
                <t3conv>1</t3conv>
            </lookindb>
        </part>
    <!--[...]-->
</uriparts>
```