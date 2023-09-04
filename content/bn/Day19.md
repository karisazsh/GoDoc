# কিভাবে আপনার স্ট্রিমলিট অ্যাপ পরিকল্পনা করবেন

এই টিউটোরিয়ালে, আমরা আমাদের স্ট্রিমলিট অ্যাপ লেআউট করতে নিম্নলিখিত কমান্ডগুলি ব্যবহার করতে যাচ্ছি:
- `st.set_page_config(layout="wide")` - অ্যাপের বিষয়বস্তুগুলি প্রশস্ত মোডে প্রদর্শন করে (অন্যথায় গতানুগতিকভাবে বিষয়বস্তুগুলি একটি নির্দিষ্ট প্রস্থের বাক্সে এনক্যাপসুলেট করা হয়।)
- `st.sidebar` - সাইডবারে উইজেট বা টেক্সট/ইমেজ ডিসপ্লে রাখে।
- `st.expander` - একটি সংকোচনযোগ্য কন্টেইনার বাক্সের ভিতরে পাঠ্য/চিত্র প্রদর্শন করে।
- `st.columns` - একটি টেবুলার স্থান (বা কলাম) তৈরি করে যার মধ্যে বিষয়বস্তু ভিতরে রাখা যেতে পারে।

## ডেমো অ্যাপ

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-layout/)

## Code
আপনার স্ট্রিমলিট অ্যাপের লেআউটটি কীভাবে কাস্টমাইজ করবেন তা এখানে:
```python
import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')
```

## লাইন-বাই-লাইন ব্যাখ্যা
স্ট্রিমলিট অ্যাপ তৈরী করার জন্য প্রথম জিনিসটি হলো `streamlit` লাইব্রেরি `st` হিসেবে ইম্পোর্ট করা:
```python
import streamlit as st
```

আমরা প্রথমে পৃষ্ঠার বিন্যাসটি সংজ্ঞায়িত করে শুরু করব যা প্রদর্শিত হবে `wide` মোড ব্যবহার করে, যা পৃষ্ঠার বিষয়বস্তুকে ব্রাউজারের প্রস্থে প্রসারিত করতে দেয়।
```python
st.set_page_config(layout="wide")
```

তারপর টাইটেল টেক্সট বানান:
```python
st.title('How to layout your Streamlit app')
```

শিরোনাম একটি প্রসারিত বাক্স `About this app` আছে এবং এটি অ্যাপ শিরোনামের অধীনে রয়েছে। সম্প্রসারণের পরে, আমরা ভিতরে অতিরিক্ত বিবরণ দেখতে পাব।
```python
with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
```

ব্যবহারকারীর ইনপুট গ্রহণ করার জন্য ইনপুট উইজেটগুলি সাইডবারে স্থাপন করা হয় `st.sidebar` কমান্ড ব্যবহার করে স্ট্রিমলিট কমান্ডস `text_input` and `selectbox` এগুলোর আগে। ব্যবহারকারীর দ্বারা প্রবেশ করা বা নির্বাচিত ইনপুট মানগুলি বরাদ্দ করা এবং সংরক্ষণ করা হয়৷ `user_name`, `user_emoji` এবং `user_food` ভেরিয়েবল দ্বারা।
```python
st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])
```

অবশেষে, আমরা ব্যবহার করে ৩টি কলাম তৈরি করব `st.columns` ব্যবহার করে `col1`, `col2` এবং `col3`। তারপর, আমরা প্রতিটি কলামে বিষয়বস্তু বরাদ্দ করি আলাদা আলাদা কোড ব্লক তৈরি করে `with` বিবৃতি দিয়ে। এর নীচে, আমরা শর্তসাপেক্ষ বিবৃতি তৈরি করি যা ব্যবহারকারী তাদের ইনপুট ডেটা (সাইডবারে নির্দিষ্ট) প্রদান করেছে কি না তার উপর নির্ভর করে ২টি বিকল্প পাঠ্যের মধ্যে ১টি প্রদর্শন করে। ডিফল্টরূপে, পৃষ্ঠাটি `else` বিবৃতির অধীনে পাঠ্য প্রদর্শন করে। ব্যবহারকারীর ইনপুট প্রদান করার পরে, ব্যবহারকারী অ্যাপে যে সংশ্লিষ্ট তথ্য দেয় তা `Output` শিরোনামের পাঠ্যের অধীনে প্রদর্শিত হয়।

```python
st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')
```
It is also worthy to note that `f` strings were used to combine pre-canned text together with the user provided values. 

## আরও পড়া
- [লেআউট এবং কন্টেইনার](https://docs.streamlit.io/library/api-reference/layout)
