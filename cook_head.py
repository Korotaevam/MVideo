import requests

cookies = {
    'MVID_ACTOR_API_AVAILABILITY': 'true',
    'MVID_BLACK_FRIDAY_ENABLED': 'true',
    'MVID_CART_AVAILABILITY': 'true',
    'MVID_CATALOG_STATE': '1',
    'MVID_CITY_ID': 'CityCZ_975',
    'MVID_COOKIE': '2500',
    'MVID_CREDIT_AVAILABILITY': 'true',
    'MVID_CREDIT_SERVICES': 'true',
    'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
    'MVID_FILTER_CODES': 'true',
    'MVID_FILTER_TOOLTIP': '1',
    'MVID_FLOCKTORY_ON': 'true',
    'MVID_GEOLOCATION_NEEDED': 'true',
    'MVID_GIFT_KIT': 'true',
    'MVID_GTM_ENABLED': '011',
    'MVID_INTERVAL_DELIVERY': 'true',
    'MVID_IS_NEW_BR_WIDGET': 'true',
    'MVID_KLADR_ID': '7700000000000',
    'MVID_LAYOUT_TYPE': '1',
    'MVID_LP_SOLD_VARIANTS': '3',
    'MVID_MCLICK': 'true',
    'MVID_MCLICK_NEW': 'true',
    'MVID_MINDBOX_DYNAMICALLY': 'true',
    'MVID_MINI_PDP': 'true',
    'MVID_NEW_ACCESSORY': 'true',
    'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
    'MVID_NEW_LK_OTP_TIMER': 'true',
    'MVID_NEW_MBONUS_BLOCK': 'true',
    'MVID_PROMO_CATALOG_ON': 'true',
    'MVID_REGION_ID': '1',
    'MVID_REGION_SHOP': 'S002',
    'MVID_SERVICES': '111',
    'MVID_TIMEZONE_OFFSET': '3',
    'MVID_TYP_CHAT': 'true',
    'MVID_WEB_SBP': 'true',
    'SENTRY_ERRORS_RATE': '0.1',
    'SENTRY_TRANSACTIONS_RATE': '0.5',
    'mindboxDeviceUUID': '307a2061-7836-4445-ab99-a934d0ee6e52',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22307a2061-7836-4445-ab99-a934d0ee6e52%22%7D',
    '_ym_uid': '1653142793946352835',
    '_ym_d': '1679504844',
    'tmr_lvid': '7325027704fe655bb5b96980546c63b2',
    'tmr_lvidTS': '1656349783356',
    'gdeslon.ru.__arc_domain': 'gdeslon.ru',
    'gdeslon.ru.user_id': '7025c904-b5d5-441d-b18a-f7193fe65d8e',
    'flocktory-uuid': '6e6d489d-69c9-4bec-a456-0dba0a1c6876-4',
    'uxs_uid': '06479590-c8d4-11ed-b193-f9f08f79dbab',
    'afUserId': 'de64c765-e795-45cb-8f18-8eec4084aadf-p',
    'adrcid': 'AiUWGEFr3sfzIeiMi_rlETA',
    '__lhash_': 'd86e3f89afa0214e268075908fab8ff8',
    'MVID_ENVCLOUD': 'prod2',
    'MVID_GLC': 'true',
    'MVID_GLP': 'true',
    '_gid': 'GA1.2.1354784515.1681634637',
    '_ym_isad': '2',
    'advcake_track_id': 'd4204e78-be4d-be4b-5202-51579a4f1c8c',
    'advcake_session_id': '78f852f7-ce7a-3965-7992-e0247bd395d4',
    'AF_SYNC': '1681634647211',
    '__SourceTracker': 'yandex.ru__organic',
    'admitad_deduplication_cookie': 'yandex.ru__organic',
    'SMSError': '',
    'authError': '',
    '__hash_': '8ac4045ececa7074370a06121cb4fb22',
    '_sp_ses.d61c': '*',
    '_dc_gtm_UA-1873769-1': '1',
    '_dc_gtm_UA-1873769-37': '1',
    'MVID_GUEST_ID': '22459318080',
    'MVID_VIEWED_PRODUCTS': '',
    'wurfl_device_id': 'generic_web_browser',
    'JSESSIONID': 'GG1Rk7WDhylhDGQrdyKXvj7pqQl4BVv7VzlQQ3Dy1W6wmMgCDtzx!1653312767',
    'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
    'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
    'MVID_CART_MULTI_DELETE': 'true',
    'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
    'MVID_GET_LOCATION_BY_DADATA': 'DaData',
    'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
    'HINTS_FIO_COOKIE_NAME': '2',
    'searchType2': '1',
    'COMPARISON_INDICATOR': 'false',
    'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
    'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
    'flacktory': 'no',
    'BIGipServeratg-ps-prod_tcp80': '1812257802.20480.0000',
    'bIPs': '434929338',
    'CACHE_INDICATOR': 'true',
    'MVID_GTM_BROWSER_THEME': '1',
    'deviceType': 'desktop',
    '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VAUmY/Ik4IM3smETk5MDJBJ2xqL1EdRAk2HGU/d0MtTn9pf3ZufDliEiZxahQkQm5RDT9DGjxrImJKWiFKW1RqJh8ZeHEnUn8SYEVKdWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeypBaSBfTmAgR1tJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=fM3InQ==',
    '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VAUmY/Ik4IM3smETk5MDJBJ2xqL1EdRAk2HGU/d0MtTn9pf3ZufDliEiZxahQkQm5RDT9DGjxrImJKWiFKW1RqJh8ZeHEnUn8SYEVKdWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeypBaSBfTmAgR1tJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=fM3InQ==',
    '_sp_id.d61c': '770db039-36f3-417f-bf48-4aa7ed047c24.1679504844.5.1681643078.1681641096.f08bd522-debf-43e2-bb4f-ce2a55a77115.a4b1f7e0-f56e-4362-b4d7-29eb7a5ecc58.025701ec-a7a1-47c9-98d0-9dced2aad82c.1681642975782.44',
    'cfidsgib-w-mvideo': 'DK0VMtqWDai0lXxx+beIL+pfdAubolD76nsw9pbkCr8Cz2cwFGcxx22hZ3DqEaTP+NsYWZ8P61F1B8AKIDdK7iY7JWlIlYAk9xJRo7tmpiQdPUalCDJp59xczzhwXzzcpnG0M/lL8nJrRSQ0nDHBkbR2BGBQ20M2ItQO',
    'cfidsgib-w-mvideo': 'DK0VMtqWDai0lXxx+beIL+pfdAubolD76nsw9pbkCr8Cz2cwFGcxx22hZ3DqEaTP+NsYWZ8P61F1B8AKIDdK7iY7JWlIlYAk9xJRo7tmpiQdPUalCDJp59xczzhwXzzcpnG0M/lL8nJrRSQ0nDHBkbR2BGBQ20M2ItQO',
    'gsscgib-w-mvideo': 'WGd/jjsfaf62jbwKFOmucOw+WJ7aMB+SghCfGssS/yePEZ7bklDeaqnduGZfM2NvB5IStOPqHpxtIBz6xD6Z0YIVCrSFq/SGFP2toD1dxSO+JV2HXWQPqCaRaCZ9Ja9w8tajeLIIPN3k/7jiGH/zMKYI6vnvIwcY6FktzZEiCnleh5CzH5uF4EDPH2SPMNTXS3ACaolz3AU9UPOkH6oifa2UeiXxzCJWh/6AaJ5YTB2V+RQY1RE04yk8+1vVPg==',
    'gsscgib-w-mvideo': 'WGd/jjsfaf62jbwKFOmucOw+WJ7aMB+SghCfGssS/yePEZ7bklDeaqnduGZfM2NvB5IStOPqHpxtIBz6xD6Z0YIVCrSFq/SGFP2toD1dxSO+JV2HXWQPqCaRaCZ9Ja9w8tajeLIIPN3k/7jiGH/zMKYI6vnvIwcY6FktzZEiCnleh5CzH5uF4EDPH2SPMNTXS3ACaolz3AU9UPOkH6oifa2UeiXxzCJWh/6AaJ5YTB2V+RQY1RE04yk8+1vVPg==',
    '_ga': 'GA1.2.1596011107.1679504844',
    'tmr_detect': '0%7C1681643080121',
    'fgsscgib-w-mvideo': '9qpj249868969094b9aba3e9f61a5752f271f573',
    'fgsscgib-w-mvideo': '9qpj249868969094b9aba3e9f61a5752f271f573',
    'cfidsgib-w-mvideo': '2kAx3k3vHM+8q6kLE1E6rQsLzhrEdx+JMYbPu78jpFVe/qBJdpIDmsyGC2YOoNe8WFpguDicNTEzciT8ANo8IXNuA29gbK7DmzoRQlKonqMUhKyGxjeFUifnwApgJQAEb9NZqEcdaBKikGZfKkPh0dNTsWpfc3f3LXHE',
    '_ga_CFMZTSS5FM': 'GS1.1.1681643005.4.1.1681643081.0.0.0',
    '_ga_BNX5WPP3YK': 'GS1.1.1681643005.4.1.1681643081.49.0.0',
}

headers = {
    'authority': 'www.mvideo.ru',
    'accept': 'application/json',
    'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
    'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=96a71eaad45d4e9493a36fa8fb8ad822,sentry-sample_rate=0.5',
    # 'cookie': 'MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_COOKIE=2500; MVID_CREDIT_AVAILABILITY=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MCLICK_NEW=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; mindboxDeviceUUID=307a2061-7836-4445-ab99-a934d0ee6e52; directCrm-session=%7B%22deviceGuid%22%3A%22307a2061-7836-4445-ab99-a934d0ee6e52%22%7D; _ym_uid=1653142793946352835; _ym_d=1679504844; tmr_lvid=7325027704fe655bb5b96980546c63b2; tmr_lvidTS=1656349783356; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=7025c904-b5d5-441d-b18a-f7193fe65d8e; flocktory-uuid=6e6d489d-69c9-4bec-a456-0dba0a1c6876-4; uxs_uid=06479590-c8d4-11ed-b193-f9f08f79dbab; afUserId=de64c765-e795-45cb-8f18-8eec4084aadf-p; adrcid=AiUWGEFr3sfzIeiMi_rlETA; __lhash_=d86e3f89afa0214e268075908fab8ff8; MVID_ENVCLOUD=prod2; MVID_GLC=true; MVID_GLP=true; _gid=GA1.2.1354784515.1681634637; _ym_isad=2; advcake_track_id=d4204e78-be4d-be4b-5202-51579a4f1c8c; advcake_session_id=78f852f7-ce7a-3965-7992-e0247bd395d4; AF_SYNC=1681634647211; __SourceTracker=yandex.ru__organic; admitad_deduplication_cookie=yandex.ru__organic; SMSError=; authError=; __hash_=8ac4045ececa7074370a06121cb4fb22; _sp_ses.d61c=*; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; MVID_GUEST_ID=22459318080; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; JSESSIONID=GG1Rk7WDhylhDGQrdyKXvj7pqQl4BVv7VzlQQ3Dy1W6wmMgCDtzx!1653312767; MVID_CALC_BONUS_RUBLES_PROFIT=true; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; HINTS_FIO_COOKIE_NAME=2; searchType2=1; COMPARISON_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; flacktory=no; BIGipServeratg-ps-prod_tcp80=1812257802.20480.0000; bIPs=434929338; CACHE_INDICATOR=true; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VAUmY/Ik4IM3smETk5MDJBJ2xqL1EdRAk2HGU/d0MtTn9pf3ZufDliEiZxahQkQm5RDT9DGjxrImJKWiFKW1RqJh8ZeHEnUn8SYEVKdWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeypBaSBfTmAgR1tJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=fM3InQ==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VAUmY/Ik4IM3smETk5MDJBJ2xqL1EdRAk2HGU/d0MtTn9pf3ZufDliEiZxahQkQm5RDT9DGjxrImJKWiFKW1RqJh8ZeHEnUn8SYEVKdWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeypBaSBfTmAgR1tJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=fM3InQ==; _sp_id.d61c=770db039-36f3-417f-bf48-4aa7ed047c24.1679504844.5.1681643078.1681641096.f08bd522-debf-43e2-bb4f-ce2a55a77115.a4b1f7e0-f56e-4362-b4d7-29eb7a5ecc58.025701ec-a7a1-47c9-98d0-9dced2aad82c.1681642975782.44; cfidsgib-w-mvideo=DK0VMtqWDai0lXxx+beIL+pfdAubolD76nsw9pbkCr8Cz2cwFGcxx22hZ3DqEaTP+NsYWZ8P61F1B8AKIDdK7iY7JWlIlYAk9xJRo7tmpiQdPUalCDJp59xczzhwXzzcpnG0M/lL8nJrRSQ0nDHBkbR2BGBQ20M2ItQO; cfidsgib-w-mvideo=DK0VMtqWDai0lXxx+beIL+pfdAubolD76nsw9pbkCr8Cz2cwFGcxx22hZ3DqEaTP+NsYWZ8P61F1B8AKIDdK7iY7JWlIlYAk9xJRo7tmpiQdPUalCDJp59xczzhwXzzcpnG0M/lL8nJrRSQ0nDHBkbR2BGBQ20M2ItQO; gsscgib-w-mvideo=WGd/jjsfaf62jbwKFOmucOw+WJ7aMB+SghCfGssS/yePEZ7bklDeaqnduGZfM2NvB5IStOPqHpxtIBz6xD6Z0YIVCrSFq/SGFP2toD1dxSO+JV2HXWQPqCaRaCZ9Ja9w8tajeLIIPN3k/7jiGH/zMKYI6vnvIwcY6FktzZEiCnleh5CzH5uF4EDPH2SPMNTXS3ACaolz3AU9UPOkH6oifa2UeiXxzCJWh/6AaJ5YTB2V+RQY1RE04yk8+1vVPg==; gsscgib-w-mvideo=WGd/jjsfaf62jbwKFOmucOw+WJ7aMB+SghCfGssS/yePEZ7bklDeaqnduGZfM2NvB5IStOPqHpxtIBz6xD6Z0YIVCrSFq/SGFP2toD1dxSO+JV2HXWQPqCaRaCZ9Ja9w8tajeLIIPN3k/7jiGH/zMKYI6vnvIwcY6FktzZEiCnleh5CzH5uF4EDPH2SPMNTXS3ACaolz3AU9UPOkH6oifa2UeiXxzCJWh/6AaJ5YTB2V+RQY1RE04yk8+1vVPg==; _ga=GA1.2.1596011107.1679504844; tmr_detect=0%7C1681643080121; fgsscgib-w-mvideo=9qpj249868969094b9aba3e9f61a5752f271f573; fgsscgib-w-mvideo=9qpj249868969094b9aba3e9f61a5752f271f573; cfidsgib-w-mvideo=2kAx3k3vHM+8q6kLE1E6rQsLzhrEdx+JMYbPu78jpFVe/qBJdpIDmsyGC2YOoNe8WFpguDicNTEzciT8ANo8IXNuA29gbK7DmzoRQlKonqMUhKyGxjeFUifnwApgJQAEb9NZqEcdaBKikGZfKkPh0dNTsWpfc3f3LXHE; _ga_CFMZTSS5FM=GS1.1.1681643005.4.1.1681643081.0.0.0; _ga_BNX5WPP3YK=GS1.1.1681643005.4.1.1681643081.49.0.0',
    'referer': 'https://www.mvideo.ru/televizory-i-cifrovoe-tv-1/televizory-65?from=under_search',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '96a71eaad45d4e9493a36fa8fb8ad822-85ee796b40d77ab0-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'x-set-application-id': '7b400731-a350-4a1f-a741-38d80398a1d9',
}

params = {
    'categoryId': '65',
    'offset': '0',
    'limit': '24',
    'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
    'doTranslit': 'true',
}


