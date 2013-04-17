# Frequently Asked Questions
- template: jobcontrol.html
- submenu: faq
---------------------

# Frequently Asked Questions
Didn't find your question below? Please [find support](support).

### When adding a job, I don't see any values in the MM-relation fields even though I've added them.
Set the "General Records Storage page" option on the sysfolder so it points to itself.

### I can't get the substitutePageTitle option fill the register value, to overwrite the title field
First of all, the content subpart must be loaded before the TypoScript part that uses the register value, otherwise the JobControl code hasn't had the chance yet to actually make the register value. So experiment with the order of loading things in your TypoScript. Also, if you use JobControl from before version 1.7.0 with the "Road 2" approach, with the TypoScript example that was given in this manual, remove these lines that used to be in that example:

```text
# clear main content in page object
page.10.subparts.CONTENT >
```

### How can I filter the job list to only show jobs from a certain region / category / etc?
You can set a custom whereadd in TypoScript. You'll need access to your database to find out the exact query to make, but it shouldn't be harder then something like this:

```text
plugin.tx_dmmjobcontrol_pi1.whereadd = uid IN (SELECT uid_local FROM tx_dmmjobcontrol_job_region_mm WHERE uid_foreign = 123
```
