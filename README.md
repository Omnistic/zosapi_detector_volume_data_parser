# zosapi_detector_volume_data_parser

My reply to this Zemax Community post to exctract Detector Volume (3D) data with the ZOSAPI: https://community.zemax.com/zos-api-12/get-data-for-volume-detector-in-zos-api-4998

Presently, it doesn't look like one can extract a 3D ```DataGrid``` from the Detector Viewer analysis in the ZOSAPI. It should be possible to extract the ```DataGrid``` for each ```Zplane``` but it feels like an overkill. Instead, I think it is simpler to save the whole data as a text file and parse it.
