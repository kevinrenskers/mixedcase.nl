# Administrators
- template: jobcontrol.html
- submenu: admins
---------------------

# Administration
This section will explain how to set up the extension so it will be showing jobs on your website. Information about adding jobs can be found in the Users manual chapter. Warning: some basic knowledge of creating extension-templates and inserting plugins on a page is expected here.


## Installation
Simply go to the extension manager, choose "Import extensions"  and search for `dmmjobcontrol`. Install the extension and let it make any tables it requires. That's it, no configuration is needed at this point.


## Styling
No default css styles are applied with JobControl, because no site should look the same. All html elements have classes assigned though, so it's very easy to style the extension to your specific needs. Basic css knowledge is of course required.


## Setting up rights
You as an administrator can add jobs just fine, but normal users without admin rights need a couple of specific rights to be able to enter all fields. You should make a new usergroup, for example "Job editors", and set the checkbox "Include Access Lists". Under "Tables (listing)" and under "Tables (modify)" select all six JobControl related items. Under "Allowed excludefields"  you should select all JobControl related fields that the user should be able to enter. If your site doesn't use a certain field, you can just disable it here and it won't even show on the form where you add jobs.

Don't forget to add your users to the new group.


## Setting up the extension
Now that you've installed JobControl on your TYPO3 server, you can start to use it on your site. There are basically two ways to set it up. In this manual they are called "**Road 1**" and "**Road 2**". The second one is the preferred method.

### Road 1: separate list- and detail pages

#### Step 1
Make two normal pages and one sysfolder page. A simple page-tree would look something like this:

#### Step 2
Add a new plugin element on both normal pages, and set it to JobControl. On the list-page ("Jobs" in our example) click on the LIST item. On the details-page ("Details") choose DETAIL instead.

#### Step 3
To make sure that the extension knows where to look for the jobs database, you should either:

1. Set the startingpoint in both plugins to the sysfolder you've created that will hold all jobs, or
2. Set the "General Records Storage page" option on the root of your page to the sysfolder containing the jobs. This is the easiest way, because it saves you from selecting a startingpoint multiple times. On the other hand. if you have another extension that requires you to set the General Records Storage page option for itself, you're stuck with the startingpoint approach.

#### Step 4
You should now configure the extension. Create an extension-template on the Jobs page, and go to the Constant Editor. Choose the category `PLUGIN.TX_DMMJOBCONTROL_PI1` and set both PID options. This is required, or the extension won't be able to create links to detailpages and back to the listpage. For an explanation of the other options please refer to the Configuration chapter in this manual.


### Road 2: list- and detail view on the same page (the preferred method)

#### Step 1
Create one normal page and one sysfolder that will contain all the jobs.

#### Step 2
You don't need to add a plugin to the normal page. Instead, you should make an extension-template on the page and paste this code into the Setup section:

```text
# default to LIST view
plugin.tx_dmmjobcontrol_pi1.display = LIST

# prevent indexing of the LIST view
config.index_enable = 0

[globalVar = GP:tx_dmmjobcontrol_pi1|job_uid > 0]
  # set code to DETAIL if the GETvar tx_dmmjobcontrol_pi1[job_uid] exists
  plugin.tx_dmmjobcontrol_pi1.display = DETAIL

  # enable indexing of the DETAIL view
  config.index_enable = 1
[global]

# load dmmjobcontrol as content to the page object
page.10.subparts.CONTENT < plugin.tx_dmmjobcontrol_pi1
```

With that code inserted, either the listview or the detailview will be shown, not both at the same time.

Compared to the other way of setting up the extension ("Road 1"), this saves you from creating an extra page, adding plugins to pages and setting up the PID values with the Constant Editor. These values or not needed because both the list- and the detailviews are on the same page, and as such links to either one are basically just links to page itself.

#### Step 3
To let JobControl know where to look for the jobs, you should either set the "General Records Storage page" option, or insert the JobControl plugin on the page and only set the startingpoint (not the "what to display" option, since this is set with TypoScript!).
