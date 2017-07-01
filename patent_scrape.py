__author__ = "Jerry He"

from subprocess import check_output,CalledProcessError
from time import sleep

def do_shell(args):
    """automatic retries"""
    if isinstance(args, str):
        args = args.split(" ")
    while True:
        try:
            return check_output(args)
        except CalledProcessError as e:
            sleep(4)
            print("Shell cmd failed with ",args)
  
  def getpatent(app_url):
    pat_num = app_url.split("?")[0]
    return do_shell(['/usr/bin/osascript', '-l','JavaScript', '/Users/jerryhe/Documents/grabPatent.scpt']+[pat_num])
    
 from dateutil.parser import parse as date_parse
 def process(a):
    for _field in [u'abstract', u'usptolink',u'filing date',u'issue date']:
        if len(a[_field])==1:
            a[_field]=a[_field][0].strip()
            if _field.endswith('date'):
                try:
                    a[_field]= date_parse(a[_field])
                except Exception as e:
                    print(e) # probably because date is badly formed
    return a
  
for doc in collection.find({}):
    if 'gpatlink' in doc:
        continue
    patnum = doc['patnum']
    if not utility_pat.match(patnum):
        continue
    ans_ = getpatent(patnum)
    try:
        a = json.loads(ans_)
        if '_id' in a:
            a['gpatlink'] = a.pop('_id')
        doc.update(process(a))
        collection.save(doc)
    except Exception as e:
        print(e)
