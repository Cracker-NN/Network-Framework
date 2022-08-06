iplocate = """
▪( IP Locate )
        |
        |
        |----------------->( Victim Information Found )
        |                           |
        |                           |-------------> ( Location)
        |                           |------------> ( Latitude and Longitude )
        |                           |-----------> ( TimeZone )
        |                           |----------> ( Carrier )
        |                           |---------> ( Country Code )
        |                           |--------> ( Pin Code )
        |
        |-------------------> ( Arguments )
                                    |
                                    |-----> ip_locate <public ip address>
                                    |-----> Parameters = 1
"""
honeypot = """
\033[1;37m
▪( HoneyPot )
        |
        |---------->( Templates )
        |               |
        |               |------------> ( denied )
        |               |-----------> ( 402 )
        |               |----------> ( error )
        |               |---------> ( not_found )
        |               |--------> ( matrix )
        |
        |------------>( Arguments )
                            |
                            |------> honeypot <ip address> <template>
                            |------> Parameters = 2
\033[0m"""

phone_number = """
▪( Phone Number )
        |
        |
        |--------------->( Victim Information Found )
        |                       |
        |                       |------------> ( SIM First Location )
        |                       |-----------> ( Latitude and Longitude)
        |                       |----------> ( Country Code )
        |                       |---------> ( TimeZone )
        |                       |--------> ( ISP )
        |                       |-------> ( Location )
        |
        |---------------> ( Arguments )
                                |
                                |----> phone_no < PhoneNumber >
                                |----> parameters = 1
"""

mail = """
▪( Email Scan )
        |
        |
        |--------------->( Victim Information Found )
        |                       |
        |                       |------------>( Email Verifying )
        |                       |----------->( Domain Checking )
        |                       |---------->( SocialMedia Account Email Verifying )
        |                                               |
        |                                               |---------->( Twitter )        
        |                                               |---------->( Instagram )
        |                                               |---------->( Spotify )
        |                                               |---------->( GitHub )
        |                                               |---------->( Petrone )
        |                                               |---------->( Pinterest )
        |                                               |---------->( WordPress )
        |                                               |---------->( Quora )
        |                                               |---------->( Google )
        |                                               |---------->( Yahoo )
        |                                               |---------->( Flickr )
        |                                               |---------->( Docker )
        |                                               |---------->( Amazon )
        |                                               |---------->( Nike )
        |                                               |---------->( Samsung )
        |                                               |---------->( X site's )
        |
        |
        |----------------> ( Arguments )
                                |-------> email_sc < Email Address >
                                |-------> parameters = 1
"""

web_sc_adv = """
▪( Web Scan Advance )
        |
        |
        |---------------->( Websites Information )
        |                        |
        |                        |------> ( Basic Information )
        |                        |                |
        |                        |                |----> Web Scan 
        |                        |                          |
        |                        |                          |---> Normal Content ( Basic Scan )
        |                        |
        |                        |------> ( CMS )
        |                        |           |
        |                        |           |----> WordPress
        |                        |           |----> Jholo
        |                        |
        |                        |-------> ( Url Scrap )
        |                                        |
        |                                        |---> https
        |
        |--------------->( Arguments )
                                |
                                |----> web_sc_adv < Url >
                                |----> Parameter = 1

"""

url_scrap = """
▪( Url Scrap )
        |
        |
        |------------->( Arguments )
                                |
                                |----> url_scr < url >
                                |----> Parameter = 1 

"""
url_capturing = """
▪( Url Tag Capture )
        |
        |
        |-------->( Arguments )
                        |
                        |-----> url_cp < url > < Tag >
                        |-----> Parameter = 2

"""

web_scan = """
▪( Web Scanning )
        |
        |
        |--------->( Website Information )
        |                     |   
        |                     |-----> Status Code
        |                     |-----> Json File
        |                     |-----> Redirecting info
        |                     |-----> Cookies
        |                     |-----> Reason
        |                     |-----> Encoding
        |
        |----------> ( Arguments )
                        |
                        |----> web_sc < url >
                        |----> Parameter = 1
"""
MAC_Locater = """
▪( MAC_Locater )
        |
        |
        |-------->( MAC Information )
        |               |
        |               |---> Company Name
        |               |---> Type
        |               |---> Country
        |               |---> Address
        |
        |-------> ( Arguments )
                        |
                        |---> MAC_Locater < MAC >
                        |---> Parameter = 1

"""
