# JSON Field in Odoo 15
This README will guide you through the process of creating a custom field in Odoo 15 that stores data as a JSON object.

## Prerequisites
1. Familiarity with Python and Odoo framework
2. Access to an Odoo instance with version 15 or above

## Steps
1. Create a new Python class called JsonField that inherits from the fields.Field class. This class will define the methods required to handle the storage and retrieval of JSON data in Odoo.
2. Override the `convert_to_cache` and `convert_to_record` methods of the Field class.
3. The `convert_to_cache` method is used to convert the JSON data stored in the database to a Python dictionary. This method takes in a string value, which represents the JSON data stored in the database, and returns a Python dictionary that can be used in memory.
4. The `convert_to_record` method is used to convert the Python dictionary back to a string that can be stored in the database. This method takes in a Python dictionary value, and returns a string representation of the JSON data. 
5. In your Odoo model, define the new custom field using the JsonField class.
6. Set `widget` attribute to 'text' in the xml file to get a input field in UI:
        
        <field name="additional_data" widget="text" />
7. Update your Odoo module and check the field in the model form view. The field should be able to store data as a JSON object and retain its format when retrieved.

## Conclusion
With these steps, you can now create a custom JSON field in Odoo 15 to store complex data structures in a more organized manner. This can be useful for storing structured data that cannot be effectively stored in a traditional text or varchar field.
