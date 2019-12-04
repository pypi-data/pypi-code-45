import requests
from bs4 import BeautifulSoup
import re
import json
import datetime
from dateutil import tz

class NSWAirQuality(object):
    """
    Returns a ```NSWAirQuality``` object, takes 1 argument, url.

    """
    def __init__(self, url=None):
        self._resourceURL = url if url else "https://airquality.environment.nsw.gov.au/aquisnetnswphp/getPage.php?reportid=2"
        response = requests.get(self._resourceURL)
        if not (response.status_code >= 200 and response.status_code <= 299):
            return
        tzinfo=tz.gettz('Australia/Sydney')
        self._retrieved = datetime.datetime.now(tz=tzinfo)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        published_date_href = soup.find('td', attrs={'class':'date'}).a['href']
        if published_date_href:
            published_date_regex = re.compile('date=(?P<year>\d\d\d\d)(?P<month>\d\d)(?P<day>\d\d)(?P<hour>\d\d)(?P<minute>\d\d)(?P<second>\d\d)(?:\D|$)',re.MULTILINE | re.IGNORECASE)
            published_date_data = published_date_regex.search(published_date_href)
            if published_date_data:
                dt = datetime.datetime(year=int(published_date_data.group('year')), month=int(published_date_data.group('month')), day=int(published_date_data.group('day')), hour=int(published_date_data.group('hour')), minute=int(published_date_data.group('minute')), second=int(published_date_data.group('second')),tzinfo=tzinfo)
                if dt:
                    self._published = dt
        data = []
        headerdata = []
        table = soup.find('table', attrs={'class':'aqi'})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        regexdatarowclass = re.compile('\w+')
        for row in rows:
            cols = row.find_all('td', {"class" : regexdatarowclass})
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols])
            #data.append([ele for ele in cols if ele]) # Get rid of empty values
            cols = row.find_all('th')
            cols = [ele.text.strip() for ele in cols]
            headerdata.append([ele for ele in cols if ele]) # Get rid of empty values
        sensors = []
        headerposition = 0
        headerrowcount = 0
        for header in headerdata:
            if headerrowcount == 0:
                sensors = header[1:]
            if headerrowcount == 1:
                for index,item in enumerate(header[1:]):
                    if item.startswith('1-hour'):
                        sensors[index] += ' 1hr Avg'
                    elif item.startswith('rolling4-hour'):
                        sensors[index] += ' 4hr Avg'
                    elif item.startswith('rolling8-hour'):
                        sensors[index] += ' 8hr Avg'
                    elif item.startswith('rolling24-hour'):
                        sensors[index] += ' 24hr Avg'
                    elif len(item) > 0:
                        sensors[index] += ' ' + item
            headerrowcount += 1
        region = None;
        for location_data in data:
            if len(location_data) > len(sensors):
                if(len(location_data) == len(sensors) + 2):
                    region = location_data.pop(0)
                site = location_data.pop(0)
                site_data = SensorData(sensors, location_data)
                if region:
                    if not hasattr(self, region):
                        setattr(self, region, Region())
                    aq_region = getattr(self, region)
                    if not hasattr(aq_region, site):
                        setattr(aq_region, site, site_data)

    def toObject(self):
        "Returns a nested object."
        data = {
            "regions": {},
            "from_url": None,
            "published": None
        }
        region = None;
        for region in self.__dict__:
            if region == "_resourceURL":
                data["from_url"] = getattr(self, "_resourceURL")
                continue
            if region == "_published":
                data["published"] = int(getattr(self, "_published").timestamp())
                continue
            if region == "_retrieved":
                data["retrieved"] = int(getattr(self, "_retrieved").timestamp())
                continue
            if not hasattr(data["regions"], region):
                data["regions"][region] = {}
            region_site_data = getattr(self, region)
            for site in region_site_data.__dict__:
                data["regions"][region][site] = getattr(region_site_data, site).__dict__
        return data

    def toJSON(self, pretty=False):
        "Returns a string containing JSON."
        data = self.toObject()
        if not pretty:
            return json.dumps(data)
        return json.dumps(data, sort_keys=True,indent=4, separators=(',', ': '))

class SensorData(object):
    """
    Returns a ```SensorData``` object, takes 2 arguments, sensors, data.

    """
    def __init__(self, sensors, data=None):
        for index,item in enumerate(sensors):
            setattr(self, item.split("\n")[0], float(data[index]) if data[index] else None)

class Sites(object):
    pass

class Region(object):
    pass
