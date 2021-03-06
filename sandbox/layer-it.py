import datetime

my_data = [
    {'event_date': '18-06-2015', 'fatalities': 9.0, 'eventname': 'Charleston, South Carolina'},
    {'event_date': '16-07-2015', 'fatalities': 5.0, 'eventname': 'Chattanooga, Tennessee'},
    {'event_date': '23-05-2014', 'fatalities': 7.0, 'eventname': 'Isla Vista, California'},
    {'event_date': '20-02-2014', 'fatalities': 4.0, 'eventname': 'Alturas, California'},
    {'event_date': '24-10-2014', 'fatalities': 5.0, 'eventname': 'Marysville, Washington'},
    {'event_date': '07-06-2013', 'fatalities': 6.0, 'eventname': 'Santa Monica, California'},
    {'event_date': '16-09-2013', 'fatalities': 13.0, 'eventname': 'Washington Navy Yard, Washington, D.C.'},
    {'event_date': '26-07-2013', 'fatalities': 6.0, 'eventname': 'Hialeah, Florida'},
    {'event_date': '21-04-2013', 'fatalities': 5.0, 'eventname': 'Federal Way, Washington'},
    {'event_date': '13-03-2013', 'fatalities': 5.0, 'eventname': 'Herkimer, New York'},
    {'event_date': '20-07-2012', 'fatalities': 12.0, 'eventname': 'Aurora, Colorado'},
    {'event_date': '05-08-2012', 'fatalities': 7.0, 'eventname': 'Oak Creek, Wisconsin'},
    {'event_date': '27-09-2012', 'fatalities': 7.0, 'eventname': 'Minneapolis, Minnesota'},
    {'event_date': '14-12-2012', 'fatalities': 27.0, 'eventname': 'Newtown, Connecticut'},
    {'event_date': '02-04-2012', 'fatalities': 7.0, 'eventname': 'Oakland, California'},
    {'event_date': '22-02-2012', 'fatalities': 5.0, 'eventname': 'Norcross, Georgia'},
    {'event_date': '20-05-2012', 'fatalities': 6.0, 'eventname': 'Seattle, Washington'},
    {'event_date': '16-04-2007', 'fatalities': 33.0, 'eventname': 'Blacksburg, Virginia'},
    {'event_date': '16-10-1991', 'fatalities': 24.0, 'eventname': 'Killeen, Texas'},
    {'event_date': '18-07-1984', 'fatalities': 21.0, 'eventname': 'San Ysidro, California'},
    #{'event_date': '01-08-1966', 'fatalities': 18.0, 'eventname': 'Incident Name'},
    {'event_date': '20-08-1986', 'fatalities': 15.0, 'eventname': 'Edmond, Oklahoma'},
    {'event_date': '05-11-2009', 'fatalities': 13.0, 'eventname': 'Fort Hood, Texas'},
    {'event_date': '03-04-2009', 'fatalities': 13.0, 'eventname': 'Binghamton, New York'},
    {'event_date': '29-11-2009', 'fatalities': 4.0, 'eventname': 'Parkland, Washington'},
    {'event_date': '20-04-1999', 'fatalities': 13.0, 'eventname': 'Littleton, Colorado'},
    {'event_date': '18-02-1983', 'fatalities': 13.0, 'eventname': 'Seattle, Washington'},
    #{'event_date': '05-09-1949', 'fatalities': 13.0, 'eventname': 'Incident Name'},
    {'event_date': '29-07-1999', 'fatalities': 12.0, 'eventname': 'Atlanta, Georgia'},
    {'event_date': '10-03-2009', 'fatalities': 10.0, 'eventname': 'Geneva County, Alabama'},
    {'event_date': '21-03-2005', 'fatalities': 10.0, 'eventname': 'Red Lake, Minnesota'},
    {'event_date': '18-06-1990', 'fatalities': 10.0, 'eventname': 'Jacksonville, Florida'},
    {'event_date': '14-10-2011', 'fatalities': 8.0, 'eventname': 'Seal Beach, California'},
    {'event_date': '03-08-2010', 'fatalities': 9.0, 'eventname': 'Manchester, Connecticut'},
    {'event_date': '19-01-2010', 'fatalities': 5.0, 'eventname': 'Appomattox, Virginia'},
    {'event_date': '29-03-2009', 'fatalities': 8.0, 'eventname': 'Carthage, North Carolina'},
    {'event_date': '05-12-2007', 'fatalities': 8.0, 'eventname': 'Omaha, Nebraska'},
    {'event_date': '01-07-1993', 'fatalities': 8.0, 'eventname': 'San Francisco, California'},
    {'event_date': '14-09-1989', 'fatalities': 8.0, 'eventname': 'Louisville, Kentucky'},
    {'event_date': '20-08-1982', 'fatalities': 8.0, 'eventname': 'Miami, Florida'},
    {'event_date': '17-01-1989', 'fatalities': 5.0, 'eventname': 'Stockton, California'},
    {'event_date': '01-11-1991', 'fatalities': 6.0, 'eventname': 'Iowa City, Iowa'},
    {'event_date': '01-05-1992', 'fatalities': 4.0, 'eventname': 'Olivehurst, California'},
    {'event_date': '07-12-1993', 'fatalities': 6.0, 'eventname': 'Garden City, New York'},
    {'event_date': '24-03-1998', 'fatalities': 5.0, 'eventname': 'Jonesboro, Arkansas'},
    {'event_date': '30-12-1999', 'fatalities': 5.0, 'eventname': 'Tampa, Florida'},
    {'event_date': '15-09-1999', 'fatalities': 7.0, 'eventname': 'Fort Worth, Texas'},
    {'event_date': '02-11-1999', 'fatalities': 7.0, 'eventname': 'Honolulu, Hawaii'},
    {'event_date': '26-12-2000', 'fatalities': 7.0, 'eventname': 'Wakefield, Massachusetts'},
    {'event_date': '08-07-2003', 'fatalities': 7.0, 'eventname': 'Meridian, Mississippi'},
    {'event_date': '02-10-2006', 'fatalities': 5.0, 'eventname': 'Lancaster County, Pennsylvania'},
    {'event_date': '25-03-2006', 'fatalities': 7.0, 'eventname': 'Capitol Hill, Washington'},
    {'event_date': '30-01-2006', 'fatalities': 8.0, 'eventname': 'Goleta, California'},
    {'event_date': '12-02-2007', 'fatalities': 5.0, 'eventname': 'Salt Lake City, Utah'},
    {'event_date': '14-02-2008', 'fatalities': 6.0, 'eventname': 'DeKalb, Illinois'},
    {'event_date': '06-09-2011', 'fatalities': 5.0, 'eventname': 'Carson City, Nevada'},
    {'event_date': '08-01-2011', 'fatalities': 6.0, 'eventname': 'Tucson, Arizona'},
    {'event_date': '29-06-1984', 'fatalities': 6.0, 'eventname': 'Dallas, Texas'},
    {'event_date': '23-04-1987', 'fatalities': 7.0, 'eventname': 'Palm Bay, Florida'},
    {'event_date': '16-02-1988', 'fatalities': 7.0, 'eventname': 'Sunnyvale, California'},
    {'event_date': '14-11-1991', 'fatalities': 5.0, 'eventname': 'Royal Oak, Michigan'},
    {'event_date': '15-10-1992', 'fatalities': 5.0, 'eventname': 'Watkins Glen, New York'},
    {'event_date': '06-08-1993', 'fatalities': 4.0, 'eventname': 'Fayetteville, North Carolina'},
    {'event_date': '14-12-1993', 'fatalities': 4.0, 'eventname': 'Aurora, Colorado'},
    {'event_date': '20-06-1994', 'fatalities': 5.0, 'eventname': 'Fairchild Air Force Base, Washington'},
    {'event_date': '03-04-1995', 'fatalities': 6.0, 'eventname': 'Corpus Christi, Texas'},
    {'event_date': '09-02-1996', 'fatalities': 6.0, 'eventname': 'Fort Lauderdale, Florida'},
    {'event_date': '15-09-1997', 'fatalities': 4.0, 'eventname': 'Aiken, South Carolina'},
    {'event_date': '18-12-1997', 'fatalities': 5.0, 'eventname': 'Orange, California'},
    {'event_date': '21-05-1998', 'fatalities': 4.0, 'eventname': 'Springfield, Oregon'},
    {'event_date': '06-03-1998', 'fatalities': 5.0, 'eventname': 'Newington, Connecticut'},
    {'event_date': '05-02-2001', 'fatalities': 5.0, 'eventname': 'Melrose Park, Illinois'},
    {'event_date': '08-12-2004', 'fatalities': 5.0, 'eventname': 'Columbus, Ohio'},
    {'event_date': '12-03-2005', 'fatalities': 7.0, 'eventname': 'Brookfield, Wisconsin'},
    {'event_date': '07-10-2007', 'fatalities': 6.0, 'eventname': 'Crandon, Wisconsin'},
    {'event_date': '25-06-2008', 'fatalities': 6.0, 'eventname': 'Henderson, Kentucky'},
    {'event_date': '07-02-2008', 'fatalities': 6.0, 'eventname': 'Kirkwood, Missouri'}
    #{'event_date': '02-04-2009', 'fatalities': 7.0, 'eventname': 'Incident Name'}
]

data_by_frequency = []

for d in my_data:
    for x in xrange(0, int(d['fatalities'])):
        #json
        #print "{'event_date': '" + str(d['event_date']) + "', 'fatalities': " + str(float(x+1)) + ", 'total': " + str(d['fatalities']) + ", 'eventname': 'Chattanooga'},"

        #csv
        print str( datetime.datetime.strptime(d['event_date'], '%d-%m-%Y') ) + ", " + str(float(x+1)) + ", " + str(d['fatalities']) + ", " + str(d['eventname'])