# Extending JobControl
- template: jobcontrol.html
- submenu: extending
---------------------

# Extending JobControl

It's fairly easy to extend JobControl with extra fields. So if you, for example, need to add a logo to a job, you can add a new "logo" field. This can be done in a few pretty easy steps:

1. Use the kickstarter to make a new extension, that modifies the JobControl database. Go to the extension manager and choose the option "Make new extension". If that option if unavailable, you need to install the kickstarter extension first.
2. In the kickstarter, first enter an extension key. This can be anything you like, for example `jobcontrolextension`.  Click on the update button to save the extension key.
3. Then click on the plus icon next to "Extend existing tables". Choose the `tx_dmmjobcontrol_job` database to work on. Enter the name and title for the new field and choose the type (in our example: "files"). Then click the update button to see all available options for the type you've chosen. Repeat if you want to add more then one field.
4. Once you're done, you can click on the "View result" button. Then you can save the extension by clicking on the "WRITE" button.
5. Install the extension and let it modify the database.

Now you have added new fields to the database, and when you add a new job you should see the new field in the form. But, the default html templates won't have any codes to show these new fields, so you need to use your own html templates to show them. Using your own templates is done with TypoScript code like this:

```text
plugin.tx_dmmjobcontrol_pi1.template.detail = fileadmin/detail.tmpl
```

In your own template you can then add a marker like `###LOGO###` but you will see that this marker won't get replaced by an actual image because the JobControl code doesn't recognize this marker. This is where the last step comes in, where you extend the markers known by JobControl.

1. Create a new file `fileadmin/markerArrayFunction.php` (or any other name you like). This file should contain one php function called `user_markerArrayFunction`. See the file [res/markerArrayFunction.php](https://github.com/kevinrenskers/dmmjobcontrol/blob/master/res/markerArrayFunction.php) for an example on how to set this up!
2. Use this TypoScript code to load the function:

```text
# Include the php script containing the function to extend the markerArray
includeLibs.markerArrayFunction = fileadmin/markerArrayFunction.php

# Call the function in the file we've just included
plugin.tx_dmmjobcontrol_pi1.markerArrayFunction = user_markerArrayFunction
```


## Extending the (multilingual) labels
Once you've added new fields to JobControl, you'll probably also need labels to use in your template. Instead of using hardcoded (non-multilingual) strings in your html template, you can extend the available labels with your own.

1. Create a new file `fileadmin/labelArrayFunction.php` (or any other name you like). This file should contain one php function called `user_labelArrayFunction`. See the file [res/labelArrayFunction.php](https://github.com/kevinrenskers/dmmjobcontrol/blob/master/res/labelArrayFunction.php) for an example on how to set this up!
2. Use this TypoScript code to load the function:

```text
# Include the php script containing the function to extend the markerArray for the labels
includeLibs.labelArrayFunction = fileadmin/labelArrayFunction.php

# Call the function in the file we've just included
plugin.tx_dmmjobcontrol_pi1.labelArrayFunction = user_labelArrayFunction
```


## Extending the search form
If you've added a new field to JobControl using the method above, you might want to add this field to the searchform. This can be done by using your own search template and create a new marker somewhere. Then to parse this marker so that a selectbox or textfield is shown, follow these steps:

1. Create a new file `fileadmin/searchArrayFunction.php` (or any other name you like). This file should contain one php function called `user_searchArrayFunction`. See the file [res/searchArrayFunction.php](https://github.com/kevinrenskers/dmmjobcontrol/blob/master/res/searchArrayFunction.php) for an example on how to set this up!
2. Use this TypoScript code to load the function:

```text
# Include the php script containing the function to extend the markerArray for the search form
includeLibs.searchArrayFunction = fileadmin/searchArrayFunction.php

# Call the function in the file we've just included
plugin.tx_dmmjobcontrol_pi1.searchArrayFunction = user_searchArrayFunction
 ```


## Extending the apply form
It's possible to extend the apply form, so you're not stuck with the predefined fields.

Create your own html template using the default apply.tmpl as an example. Add your new field, for example something like this.

```html
<tr class="dmmjobcontrol_apply_tr">
  <td class="dmmjobcontrol_apply_td1">
    ###ADDRESS_LABEL###
  </td>
  <td class="dmmjobcontrol_apply_td2">
    <input type="text" name="###ADDRESS_NAME###" value="###ADDRESS_VALUE###" class="dmmjobcontrol_input" />
  </td>
</tr>
```

To use your custom template, use this typoscript code:

```text
plugin.tx_dmmjobcontrol_pi1.template.apply = fileadmin/apply.tmpl
```

1. Extend the labels using labelArrayFunction (see documentation above) so the system knows how to parse `###ADDRESS_LABEL###`.
2. Create a new file `fileadmin/applyArrayFunction.php` (or any other name you like). This file should contain one php function called `user_applyArrayFunction`. See the file [res/applyArrayFunction.php](https://github.com/kevinrenskers/dmmjobcontrol/blob/master/res/applyArrayFunction.php) for an example on how to set this up!
3. Use this TypoScript code to load the function:

```text
# Include the php script containing the function to extend the markerArray for the labels
includeLibs.applyArrayFunction = fileadmin/applyArrayFunction.php

# Call the function in the file we've just included
plugin.tx_dmmjobcontrol_pi1.applyArrayFunction = user_applyArrayFunction
```

It's important to use labelArrayFunction to add the new label, and applyArrayFunction for the other markers.

You can make this new field required by adding it to typoscript constants:

```text
plugin.dmmjobcontrol.apply.required = fullname,email,motivation,file_cv,address
```