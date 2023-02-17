data = '''          <div class="col-sm-6 col-lg-4 all %category%">
            <div class="box">
              <div>
                <div class="img-box">
                  <img src="%image%" alt="">
                </div>
                <div class="detail-box">
                  <h5>
                    %name%
                  </h5>
                  <p>
                    %comment%
                  </p>
                  <div class="options">
                    <h6>
                      %price%
                    </h6>
                  </div>
                </div>
              </div>
            </div>
          </div>'''

data = '''          <div class="col-sm-6 col-lg-4 all %category%">
            <div class="box">
              <div>
                <div class="img-box">
                  <img src="%image%" alt="">
                </div>
                <div class="detail-box">
                  <h5>
                    %name%
                  </h5>
                </div>
              </div>
            </div>
          </div>'''


import os, unicodedata
from urllib.parse import unquote, quote, quote_plus, urlencode

base = 'images/sh'
for _ in os.listdir('./'+base):
    # print(_.encode('utf-8').decode('utf-8'))
    _ = unicodedata.ucd_3_2_0.normalize('NFC', _).encode('utf-8').decode()
    # break
    if '.png' in _:
        print(data.replace('%category%', 'sh').replace('%image%', quote(base+'/'+_)).replace('%name%', _.split('-min')[0]))



base = 'images/bc'
for _ in os.listdir('./'+base):
    # print(_.encode('utf-8').decode('utf-8'))
    _ = unicodedata.ucd_3_2_0.normalize('NFC', _).encode('utf-8').decode()
    # break
    if ('.png' in _)or ('.jpg' in _) or ('.webp' in _) :
        print(data.replace('%category%', 'bc').replace('%image%', quote(base+'/'+_)).replace('%name%', _.split('.')[0]))