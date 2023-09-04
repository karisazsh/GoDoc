# স্ট্রিমলিট অ্যাপ তৈরির শিল্প

*#30DaysOfStreamlit* চ্যালেঞ্জের আজকের দিন ৩০। অভিনন্দন এই চ্যালেঞ্জে এতদূর গড়ার জন্য।

এই টিউটোরিয়ালে, আমরা বাস্তব-বিশ্বের সমস্যা সমাধানের জন্য স্ট্রিমলিট অ্যাপস তৈরি করার জন্য এই শেখার চ্যালেঞ্জ থেকে আমাদের নতুন জ্ঞান রাখতে যাচ্ছি।

## বাস্তব বিশ্বের সমস্যা

একটি বিষয়বস্তু নির্মাতা হিসাবে, ইউটিউব  ভিডিও থেকে থাম্বনেইল চিত্রগুলিতে অ্যাক্সেস থাকা সামাজিক প্রচার এবং সামগ্রী তৈরির জন্য দরকারী সংস্থান।

আসুন আমরা কীভাবে এই সমস্যাটি মোকাবেলা করতে যাচ্ছি এবং একটি স্ট্রিমলিট অ্যাপ তৈরি করব তা খুঁজে বের করা যাক।

## সমাধান

আজ, আমরা `yt-img-app` তৈরি করতে যাচ্ছি, যেটি একটি স্ট্রিমলিট অ্যাপ যা ইউটিউব  ভিডিও থেকে থাম্বনেইল ছবি বের করতে পারে।

সংক্ষেপে, এখানে ৩টি সহজ পদক্ষেপ যা আমরা স্ট্রিমলিট অ্যাপটি করতে চাই:

১. ব্যবহারকারীদের কাছ থেকে ইনপুট হিসাবে একটি ইউটিউব URL গ্রহণ করুন৷
২. ইউনিক ইউটিউব ভিডিও আইডি এক্সট্র্যাক্ট করতে URL-এর টেক্সট প্রসেসিং করুন
৩. একটি কাস্টম ফাংশনে ইনপুট হিসাবে ইউটিউব ভিডিও আইডি ব্যবহার করুন যা ইউটিউব ভিডিওগুলি থেকে থাম্বনেইল চিত্র পুনরুদ্ধার করে এবং প্রদর্শন করে

## নির্দেশনা

স্ট্রিমলিট অ্যাপ ব্যবহার শুরু করতে, ইনপুট টেক্সট বক্সে একটি ইউটিউব URL কপি করে পেস্ট করুন।

## ডেমো অ্যাপ

[![স্ট্রিমলিট অ্যাপ](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/yt-img-app/)

## কোড
এখানে কিভাবে `yt-img-app` Streamlit অ্যাপ তৈরি করবেন:
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

## লাইন-বাই-লাইন ব্যাখ্যা
একটি স্ট্রিমলিট অ্যাপ তৈরি করার সময় প্রথমেই যা করতে হবে তা হল `streamlit` লাইব্রেরিকে `st` এর মতো আমদানি করে শুরু করা:
```python
import streamlit as st
```

এর পরে, আমরা অ্যাপের শিরোনাম এবং সহকারী শিরোনাম প্রদর্শন করি:
```python
st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')
```
আমরা এটিতে থাকাকালীন, আমরা একটি সম্প্রসারণযোগ্য বাক্স সম্পর্কেও নিক্ষেপ করতে পারি।
```python
with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')
 
Here, we create selection box for accepting user input on the image quality to use.
```python
# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]
```

ইউটিউব ভিডিও URL-এ ব্যবহারকারীর ইনপুট গ্রহণ করার জন্য একটি ইনপুট টেক্সট বক্স প্রদর্শিত হয় যা থেকে ছবিটি বের করার জন্য ব্যবহার করা হয়।
```python
yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')
```

ইনপুট URL-এর পাঠ্য প্রক্রিয়াকরণের জন্য একটি কাস্টম ফাংশন।
```python
def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
```

অবশেষে, URL প্রবেশ করার জন্য একটি অনুস্মারক প্রদর্শন করা হবে কিনা তা নির্ধারণ করতে আমরা প্রবাহ নিয়ন্ত্রণ ব্যবহার করি (যেমন `else` বিবৃতিতে) অথবা ইউটিউব থাম্বনেইল চিত্র প্রদর্শন করতে (যেমন `if` বিবৃতিতে)।
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

## সারসংক্ষেপ

সংক্ষেপে, আমরা দেখেছি যে কোনও স্ট্রিমলিট অ্যাপ তৈরি করার সময়, আমরা সাধারণত প্রথমে সমস্যাটি সনাক্ত এবং সংজ্ঞায়িত করে শুরু করি। এরপরে, আমরা স্ট্রিমলিট অ্যাপে প্রয়োগ করি এমন দানাদার ধাপে বিভক্ত করে সমস্যাটি মোকাবেলা করার জন্য একটি সমাধান তৈরি করি।

এখানে, আমাদের ব্যবহারকারীদের কাছ থেকে ইনপুট হিসাবে আমাদের কোন ডেটা বা তথ্য প্রয়োজন তা নির্ধারণ করতে হবে, চূড়ান্ত পছন্দসই আউটপুট তৈরি করার জন্য ব্যবহারকারীর ইনপুট প্রক্রিয়াকরণে ব্যবহার করার পদ্ধতি এবং পদ্ধতি।

আশা করি আপনি এই টিউটোরিয়ালটি উপভোগ করেছেন, হ্যাপি স্ট্রিমলিটিং! 
