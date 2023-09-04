# Streamlit ऐप्स बनाने की कला

*#30DaysOfStreamlit</0* चैलेंज का आज का 30वां दिन|
इस चैलेंज में अब तक इसे बनाने के लिए बधाई|

इस ट्यूटोरियल में, हम वास्तविक दुनिया की समस्या को हल करने के लिए Streamlit ऐप्स बनाने के लिए, इस सीखने के चैलेंज से प्राप्त अपने नए ज्ञान को बताने जा रहे हैं|

## वास्तविक-दुनिया की समस्या

एक कान्टेन्ट निर्माता के रूप में, YouTube वीडियो से थंबनेल इमेजेज़ तक पहुंच सामाजिक प्रचार और कान्टेन्ट क्रीएशन के लिए उपयोगी संसाधन हैं|

आइए जानें कि हम इस समस्या से कैसे निपटेंगे और एक Streamlit ऐप कैसे बनाएंगे|

## समाधान

आज, हम `yt-img-app` बनाने जा रहे हैं, जो एक Streamlit ऐप है जो YouTube वीडियो से थंबनेल इमेजेज़ को निकाल सकता है|

संक्षेप में, यहां 3 आसान स्टेप्स दिए गए हैं, जो हम चाहते हैं कि Streamlit ऐप करे:

1. यूज़र से इनपुट के रूप में YouTube URL स्वीकार करें
2. यूनीक YouTube वीडियो ID निकालने के लिए URL की टेक्स्ट प्रोसेसिंग करें
3. YouTube वीडियो ID को एक कस्टम फ़ंक्शन के इनपुट के रूप में उपयोग करें जो YouTube वीडियो से थंबनेल इमेज को रिट्रीव और प्रदर्शित करता है

## निर्देश

Streamlit ऐप का उपयोग शुरू करने के लिए, इनपुट टेक्स्ट बॉक्स में एक YouTube URL कॉपी और पेस्ट करें|

## Demo ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/yt-img-app/)

## कोड
यहां `yt-img-app` Streamlit ऐप बनाने का तरीका बताया गया है:
```python
import streamlit as st

st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')

with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')
  
# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')

def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
    
# Display YouTube thumbnail image
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('☝️ Enter URL to continue ...')
```

## लाइन-बाय-लाइन स्पष्टीकरण
Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी को import करके शुरू करना है:
```python
import streamlit as st
```

इसके बाद, हम ऐप का टाइटल और साथ में हेडर प्रदर्शित करते हैं:
```python
st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')
```

जब तक हम इस पर हैं, हम विस्तार योग्य बॉक्स के बारे में भी बता सकते हैं|
```python
with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')
```
 
Here, we create selection box for accepting user input on the image quality to use.
```python
# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]
```

इमेज निकालने के लिए उपयोग करने के लिए YouTube वीडियो URL पर यूज़र इनपुट स्वीकार करने के लिए एक इनपुट टेक्स्ट बॉक्स प्रदर्शित किया जाता है.
```python
yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')
```

इनपुट URL का टेक्स्ट प्रोसेसिंग करने के लिए एक कस्टम फ़ंक्शन.
```python
def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
```


अंत में, हम यह निर्धारित करने के लिए फ़्लो कंट्रोल का उपयोग करते हैं कि URL दर्ज करने के लिए रिमाइंडर प्रदर्शित करना है या नहीं (यानी जैसा कि `else` स्टेटमेंट में है) या YouTube थंबनेल इमेज प्रदर्शित करने के लिए (यानी जैसा कि `if` स्टेटमेंट में है)|
```python
# Display YouTube thumbnail image
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('☝️ Enter URL to continue ...')
```

## सारांश

संक्षेप में, हमने देखा है कि किसी भी Streamlit ऐप के निर्माण में, हम आम तौर पर पहले समस्या की पहचान और उसे परिभाषित करके शुरू करते हैं|

इसके बाद, हम समस्या से निपटने के लिए समाधान तैयार करते हैं, इसे छोटे स्टेप्स में विभाजित करते हैं, जिसे हम Streamlit ऐप में लागू करते हैं|

यहां, हमें यूज़र से इनपुट के रूप में कौन से डेटा या जानकारी की आवश्यकता है, और अंतिम वांछित आउटपुट का उत्पादन करने के लिए यूज़र इनपुट को प्रोसेस करने के लिए दृष्टिकोण और विधि निर्धारित करने होंगे|

आशा है कि आपको यह ट्यूटोरियल अच्छा लगा होगा, हैप्पी Streamlit-ing!
