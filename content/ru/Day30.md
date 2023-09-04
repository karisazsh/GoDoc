# Day 30

# **Искусство создания приложений Streamlit**

Сегодня 30-й день задания *#30DaysOfStreamlit*. Поздравляем!

В этом уроке мы будем использовать новые знания, которые вы получили при создании приложений Streamlit для решения реальных проблем.

## **Реальная проблема**

Для создателя контента доступ к тамбнейлам YouTube видео очень важен для успеха в социальных сетях и создания контента.

Давайте решим эту проблему и создадим приложение Streamlit.

## **Решение**

Сегодня мы будем создавать `yt-img-app`, приложение Streamlit, которое может извлекать тамбнейлы из YouTube видео.

Вот три простых шага, которые Streamlit может выполнить:

1. Принятие URL-адреса YouTube в качестве входных данных от пользователей.
2. Выполнение текстовой обработки URL-адреса для извлечения уникального идентификатора видео YouTube.
3. Использование идентификатора видео YouTube в качестве входных данных для пользовательской функции, которая извлекает и отображает тамбнейл из видео YouTube.

## **Инструкции**

Чтобы начать использовать приложение Streamlit, скопируйте и вставьте URL-адрес YouTube в текстовое поле ввода.

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/yt-img-app/)

## **Код**

Как создать приложение `yt-img-app` Streamlit:

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

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st`, например:
```python
import streamlit as st
```

Затем мы покажем название приложения и сопутствующий ему заголовок:

```python
st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')
```

Здесь мы можем также добавить расширяемое поле «О программе».

```python
with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')
```
 
Здесь мы создаем поле выбора для принятия пользовательского ввода по качеству изображения для использования.
```python
# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]
```

Вы увидите изображение текстового поля для ввода URL-адреса видео YouTube, используемого для извлечения изображения.

```python
yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')
```

Вот пользовательская функция для обработки текста входного URL.
```python
def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
```

Наконец, мы используем управление потоком, чтобы определить, следует ли отображать напоминание о вводе URL-адреса (например, как в операторе `else`) или отображать тамбнейл изображения YouTube (например, как в операторе `if`).

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

## **Итог**

Подводя итог, нам становится ясно что при создании любого приложения Streamlit мы обычно начинаем с выявления и определения проблемы. Затем мы разрабатываем решение проблемы, разбиваем ее на отдельные этапы, и потом реализуем их в приложении Streamlit.

Здесь нам нужно решить, какие данные или информация нам необходимы в качестве входных данных от пользователей, а также подход и метод, которые следует использовать при обработке пользовательского ввода для получения желаемого результата.

Надеюсь, вам понравился этот урок. Счастливого Streamlit-ing!
