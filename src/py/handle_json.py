import datetime
import json
import sys
from create_docx import Asset, Accessory, create_single_asset_docx, create_user_assets_docx, create_return_form_docx

example_json = '{"id":174,"name":"","asset_tag":"00174","serial":"GFSKJG3","model":{"id":7,"name":"Latitude 5520"},"byod":false,"model_number":null,"eol":null,"asset_eol_date":null,"status_label":{"id":2,"name":"Ready to Deploy","status_type":"deployable","status_meta":"deployed"},"category":{"id":3,"name":"Laptop"},"manufacturer":{"id":3,"name":"Dell"},"supplier":null,"notes":null,"order_number":null,"company":{"id":1,"name":"Belek"},"location":{"id":1,"name":"Kullanıcılar"},"rtd_location":null,"image":null,"qr":null,"alt_barcode":"https://demirbas.megasaray.local/uploads/barcodes/c128-00174.png","assigned_to":{"id":2,"username":"o.akin","name":"Onur Akin","first_name":"Onur","last_name":"Akin","email":"o.akin@megasarayhotels.com","employee_number":null,"type":"user"},"warranty_months":null,"warranty_expires":null,"created_at":{"datetime":"2023-09-04 12:33:06","formatted":"2023-09-04 12:33 PM"},"updated_at":{"datetime":"2023-09-04 12:33:06","formatted":"2023-09-04 12:33 PM"},"last_audit_date":null,"next_audit_date":null,"deleted_at":null,"purchase_date":null,"age":"","last_checkout":{"datetime":"2023-09-04 12:33:06","formatted":"2023-09-04 12:33 PM"},"expected_checkin":null,"purchase_cost":null,"checkin_counter":0,"checkout_counter":1,"requests_counter":0,"user_can_checkout":false,"book_value":null,"custom_fields":{},"available_actions":{"checkout":true,"checkin":true,"clone":true,"restore":false,"update":true,"delete":false}}'
example_user_json = '{"total":4,"rows":[{"id":27,"name":"","asset_tag":"00027","serial":"CN02VNH80WSL001BAJJGBA04","model":{"id":20,"name":"S2721HS"},"byod":false,"model_number":null,"eol":null,"asset_eol_date":null,"status_label":{"id":2,"name":"Ready to Deploy","status_type":"deployable","status_meta":"deployable"},"category":{"id":2,"name":"Monitör"},"manufacturer":{"id":3,"name":"Dell"},"supplier":null,"notes":null,"order_number":null,"company":{"id":1,"name":"Belek"},"location":{"id":1,"name":"Kullanıcılar"},"rtd_location":null,"image":null,"qr":null,"alt_barcode":"https://demirbas.megasaray.local/uploads/barcodes/c128-00027.png","assigned_to":null,"warranty_months":null,"warranty_expires":null,"created_at":{"datetime":"2023-08-31 09:25:31","formatted":"2023-08-31 09:25 AM"},"updated_at":{"datetime":"2023-08-31 09:25:31","formatted":"2023-08-31 09:25 AM"},"last_audit_date":null,"next_audit_date":null,"deleted_at":null,"purchase_date":null,"age":"","last_checkout":{"datetime":"2023-08-31 09:25:31","formatted":"2023-08-31 09:25 AM"},"expected_checkin":null,"purchase_cost":null,"checkin_counter":0,"checkout_counter":1,"requests_counter":0,"user_can_checkout":false,"book_value":null,"custom_fields":{},"available_actions":{"checkout":true,"checkin":true,"clone":true,"restore":false,"update":true,"delete":false}},{"id":28,"name":"","asset_tag":"00028","serial":"D1304W3","model":{"id":18,"name":"Vostro 3510"},"byod":false,"model_number":null,"eol":null,"asset_eol_date":null,"status_label":{"id":2,"name":"Ready to Deploy","status_type":"deployable","status_meta":"deployable"},"category":{"id":3,"name":"Laptop"},"manufacturer":{"id":3,"name":"Dell"},"supplier":null,"notes":null,"order_number":null,"company":{"id":1,"name":"Belek"},"location":{"id":1,"name":"Kullanıcılar"},"rtd_location":null,"image":null,"qr":null,"alt_barcode":"https://demirbas.megasaray.local/uploads/barcodes/c128-00028.png","assigned_to":null,"warranty_months":null,"warranty_expires":null,"created_at":{"datetime":"2023-08-31 09:27:05","formatted":"2023-08-31 09:27 AM"},"updated_at":{"datetime":"2023-08-31 09:27:05","formatted":"2023-08-31 09:27 AM"},"last_audit_date":null,"next_audit_date":null,"deleted_at":null,"purchase_date":null,"age":"","last_checkout":{"datetime":"2023-08-31 09:27:05","formatted":"2023-08-31 09:27 AM"},"expected_checkin":null,"purchase_cost":null,"checkin_counter":0,"checkout_counter":1,"requests_counter":0,"user_can_checkout":false,"book_value":null,"custom_fields":{},"available_actions":{"checkout":true,"checkin":true,"clone":true,"restore":false,"update":true,"delete":false}},{"id":29,"name":"","asset_tag":"00029","serial":"VNFNF02564","model":{"id":21,"name":"LaserJet Pro MFP M130fw"},"byod":false,"model_number":null,"eol":null,"asset_eol_date":null,"status_label":{"id":2,"name":"Ready to Deploy","status_type":"deployable","status_meta":"deployable"},"category":{"id":6,"name":"Yazıcı"},"manufacturer":{"id":2,"name":"Hewlett-Packard"},"supplier":null,"notes":null,"order_number":null,"company":{"id":1,"name":"Belek"},"location":{"id":1,"name":"Kullanıcılar"},"rtd_location":null,"image":null,"qr":null,"alt_barcode":"https://demirbas.megasaray.local/uploads/barcodes/c128-00029.png","assigned_to":null,"warranty_months":null,"warranty_expires":null,"created_at":{"datetime":"2023-08-31 09:28:21","formatted":"2023-08-31 09:28 AM"},"updated_at":{"datetime":"2023-08-31 09:28:21","formatted":"2023-08-31 09:28 AM"},"last_audit_date":null,"next_audit_date":null,"deleted_at":null,"purchase_date":null,"age":"","last_checkout":{"datetime":"2023-08-31 09:28:21","formatted":"2023-08-31 09:28 AM"},"expected_checkin":null,"purchase_cost":null,"checkin_counter":0,"checkout_counter":1,"requests_counter":0,"user_can_checkout":false,"book_value":null,"custom_fields":{},"available_actions":{"checkout":true,"checkin":true,"clone":true,"restore":false,"update":true,"delete":false}},{"id":30,"name":"","asset_tag":"00030","serial":"T1797804956","model":{"id":4,"name":"GM21 Pro"},"byod":false,"model_number":null,"eol":null,"asset_eol_date":null,"status_label":{"id":2,"name":"Ready to Deploy","status_type":"deployable","status_meta":"deployable"},"category":{"id":4,"name":"Akıllı Telefon"},"manufacturer":{"id":4,"name":"General Mobile"},"supplier":null,"notes":null,"order_number":null,"company":{"id":1,"name":"Belek"},"location":{"id":1,"name":"Kullanıcılar"},"rtd_location":null,"image":null,"qr":null,"alt_barcode":"https://demirbas.megasaray.local/uploads/barcodes/c128-00030.png","assigned_to":null,"warranty_months":null,"warranty_expires":null,"created_at":{"datetime":"2023-08-31 09:29:11","formatted":"2023-08-31 09:29 AM"},"updated_at":{"datetime":"2023-08-31 09:29:11","formatted":"2023-08-31 09:29 AM"},"last_audit_date":null,"next_audit_date":null,"deleted_at":null,"purchase_date":null,"age":"","last_checkout":{"datetime":"2023-08-31 09:29:11","formatted":"2023-08-31 09:29 AM"},"expected_checkin":null,"purchase_cost":null,"checkin_counter":0,"checkout_counter":1,"requests_counter":0,"user_can_checkout":false,"book_value":null,"custom_fields":{},"available_actions":{"checkout":true,"checkin":true,"clone":true,"restore":false,"update":true,"delete":false}}]}'
example_return_json = '{"totalCheckins":3,"rows":[{"id":1,"name":"M330","image":"https://demirbas.megasaray.local/uploads/accessories/accessory-image-1-C4ErS60hfN.webp","company":null,"manufacturer":{"id":25,"name":"Logitech"},"supplier":null,"model_number":null,"category":{"id":15,"name":"Fare"},"location":null,"notes":null,"qty":50,"purchase_date":null,"purchase_cost":null,"order_number":null,"min_qty":null,"remaining_qty":39,"users_count":11,"created_at":{"datetime":"2023-09-16 12:43:47","formatted":"2023-09-16 12:43 PM"},"updated_at":{"datetime":"2023-09-16 13:03:45","formatted":"2023-09-16 01:03 PM"},"available_actions":{"checkout":true,"checkin":false,"update":true,"delete":true,"clone":true},"user_can_checkout":true},{"id":8,"name":"","asset_tag":"00008","serial":"DGSKJG3","model":{"id":7,"name":"Latitude 5520"},"byod":false,"model_number":null,"eol":null,"asset_eol_date":null,"status_label":{"id":2,"name":"Ready to Deploy","status_type":"deployable","status_meta":"deployed"},"category":{"id":3,"name":"Laptop"},"manufacturer":{"id":3,"name":"Dell"},"supplier":null,"notes":null,"order_number":null,"company":{"id":2,"name":"Westbeach"},"location":{"id":1,"name":"Kullanıcılar"},"rtd_location":null,"image":null,"qr":null,"alt_barcode":"https://demirbas.megasaray.local/uploads/barcodes/c128-00008.png","assigned_to":{"id":326,"username":"z.tabaldieva","name":"Zhanar Tabaldieva","first_name":"Zhanar","last_name":"Tabaldieva","email":"z.tabaldieva@megasarayhotels.com","employee_number":null,"type":"user"},"warranty_months":null,"warranty_expires":null,"created_at":{"datetime":"2023-08-29 15:15:25","formatted":"2023-08-29 03:15 PM"},"updated_at":{"datetime":"2023-09-27 12:58:37","formatted":"2023-09-27 12:58 PM"},"last_audit_date":null,"next_audit_date":null,"deleted_at":null,"purchase_date":null,"age":"","last_checkout":{"datetime":"2023-09-27 12:58:37","formatted":"2023-09-27 12:58 PM"},"expected_checkin":null,"purchase_cost":null,"checkin_counter":1,"checkout_counter":2,"requests_counter":0,"user_can_checkout":false,"book_value":null,"custom_fields":{},"available_actions":{"checkout":true,"checkin":true,"clone":true,"restore":false,"update":true,"delete":false}},{"id":9,"name":"","asset_tag":"00009","serial":"Y1820100134","model":{"id":8,"name":"GM22 Plus"},"byod":false,"model_number":null,"eol":null,"asset_eol_date":null,"status_label":{"id":2,"name":"Ready to Deploy","status_type":"deployable","status_meta":"deployed"},"category":{"id":4,"name":"Akıllı Telefon"},"manufacturer":{"id":4,"name":"General Mobile"},"supplier":null,"notes":null,"order_number":null,"company":{"id":2,"name":"Westbeach"},"location":{"id":1,"name":"Kullanıcılar"},"rtd_location":null,"image":null,"qr":null,"alt_barcode":"https://demirbas.megasaray.local/uploads/barcodes/c128-00009.png","assigned_to":{"id":326,"username":"z.tabaldieva","name":"Zhanar Tabaldieva","first_name":"Zhanar","last_name":"Tabaldieva","email":"z.tabaldieva@megasarayhotels.com","employee_number":null,"type":"user"},"warranty_months":null,"warranty_expires":null,"created_at":{"datetime":"2023-08-29 15:17:36","formatted":"2023-08-29 03:17 PM"},"updated_at":{"datetime":"2023-09-27 13:06:02","formatted":"2023-09-27 01:06 PM"},"last_audit_date":null,"next_audit_date":null,"deleted_at":null,"purchase_date":null,"age":"","last_checkout":{"datetime":"2023-09-27 13:06:02","formatted":"2023-09-27 01:06 PM"},"expected_checkin":null,"purchase_cost":null,"checkin_counter":1,"checkout_counter":2,"requests_counter":0,"user_can_checkout":false,"book_value":null,"custom_fields":{"IMEI":{"field":"_snipeit_imei_2","value":"359796367050176","field_format":"regex:/^[0-9]{15}$/","element":"text"},"MAC Adresi":{"field":"_snipeit_mac_adresi_1","value":"","field_format":"MAC","element":"text"}},"available_actions":{"checkout":true,"checkin":true,"clone":true,"restore":false,"update":true,"delete":false}}]}'

def handle_json(jsonObj: str):
    current_object = json.loads(jsonObj)
    # user assets
    if (current_object.get('totalAssets') != None):
        assets = []
        json_array = current_object.get('rows')
        for asset in json_array:
            assets.append(Asset(asset))
        create_user_assets_docx(assets, current_object.get('admin'), current_object.get('target'))
    # return form
    elif (current_object.get('totalCheckins') != None):
        items = []
        json_array = current_object.get('rows')
        for item in json_array:
            # accessory
            if item.get('asset_tag') == None:
                items.append(Accessory(item))
            # asset
            else:
                items.append(Asset(item))
        create_return_form_docx(items, current_object.get('admin'), current_object.get('target'))
    # single asset
    elif (current_object.get('asset') != None):
        current_asset = Asset(current_object.get('asset'))
        create_single_asset_docx(current_asset, current_object.get('admin'), current_object.get('target'))

handle_json(sys.argv[1])
# handle_json(example_json)
# handle_json(example_user_json)
# handle_json(example_return_json)
