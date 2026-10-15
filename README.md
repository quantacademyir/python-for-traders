# Python برای تریدرها

کد و داده‌های دوره رایگان **«Python برای تریدرها»** از [Quant Academy](https://quantacademy.ir).

۱۰ درس برای تریدرها و تحلیل‌گرهایی که برنامه‌نویسی بلد نیستند و می‌خواهند داده بازار را خودشان تحلیل کنند: از اولین سلول کد تا یک گزارش یک‌صفحه‌ای.

📚 متن درس‌ها: https://quantacademy.ir/courses/python-for-traders/

> داده‌های این دوره **شبیه‌سازی‌شده** هستند، نه قیمت واقعی بازار. هدف یاد دادن روش است.
> آموزشی است و توصیه سرمایه‌گذاری نیست.

## نوت‌بوک‌ها

هر درس یک نوت‌بوک دارد. با کلیک روی «Colab» بدون نصب چیزی در مرورگر اجرا می‌شود.

| درس | موضوع | اجرا |
|---|---|---|
| 1 | [چرا تریدر باید Python بلد باشد؟](https://quantacademy.ir/courses/python-for-traders/why-python-colab/) | [Colab](https://colab.research.google.com/github/quantacademyir/python-for-traders/blob/main/notebooks/01-why-python-colab.ipynb) · [GitHub](https://github.com/quantacademyir/python-for-traders/blob/main/notebooks/01-why-python-colab.ipynb) |
| 2 | [متغیر، لیست و دیکشنری](https://quantacademy.ir/courses/python-for-traders/variables-lists-dicts/) | [Colab](https://colab.research.google.com/github/quantacademyir/python-for-traders/blob/main/notebooks/02-variables-lists-dicts.ipynb) · [GitHub](https://github.com/quantacademyir/python-for-traders/blob/main/notebooks/02-variables-lists-dicts.ipynb) |
| 3 | [شرط، حلقه و تابع](https://quantacademy.ir/courses/python-for-traders/conditions-loops-functions/) | [Colab](https://colab.research.google.com/github/quantacademyir/python-for-traders/blob/main/notebooks/03-conditions-loops-functions.ipynb) · [GitHub](https://github.com/quantacademyir/python-for-traders/blob/main/notebooks/03-conditions-loops-functions.ipynb) |
| 4 | [گرفتن داده بازار: CSV و API](https://quantacademy.ir/courses/python-for-traders/getting-data/) | [Colab](https://colab.research.google.com/github/quantacademyir/python-for-traders/blob/main/notebooks/04-getting-data.ipynb) · [GitHub](https://github.com/quantacademyir/python-for-traders/blob/main/notebooks/04-getting-data.ipynb) |
| 5 | [DataFrame در pandas](https://quantacademy.ir/courses/python-for-traders/pandas-dataframe/) | [Colab](https://colab.research.google.com/github/quantacademyir/python-for-traders/blob/main/notebooks/05-pandas-dataframe.ipynb) · [GitHub](https://github.com/quantacademyir/python-for-traders/blob/main/notebooks/05-pandas-dataframe.ipynb) |
| 6 | [بازده ساده و لگاریتمی](https://quantacademy.ir/courses/python-for-traders/returns/) | [Colab](https://colab.research.google.com/github/quantacademyir/python-for-traders/blob/main/notebooks/06-returns.ipynb) · [GitHub](https://github.com/quantacademyir/python-for-traders/blob/main/notebooks/06-returns.ipynb) |
| 7 | [میانگین متحرک و rolling](https://quantacademy.ir/courses/python-for-traders/moving-average-rolling/) | [Colab](https://colab.research.google.com/github/quantacademyir/python-for-traders/blob/main/notebooks/07-moving-average-rolling.ipynb) · [GitHub](https://github.com/quantacademyir/python-for-traders/blob/main/notebooks/07-moving-average-rolling.ipynb) |
| 8 | [تمیز کردن داده و resample](https://quantacademy.ir/courses/python-for-traders/cleaning-resample/) | [Colab](https://colab.research.google.com/github/quantacademyir/python-for-traders/blob/main/notebooks/08-cleaning-resample.ipynb) · [GitHub](https://github.com/quantacademyir/python-for-traders/blob/main/notebooks/08-cleaning-resample.ipynb) |
| 9 | [نمودار با matplotlib](https://quantacademy.ir/courses/python-for-traders/matplotlib/) | [Colab](https://colab.research.google.com/github/quantacademyir/python-for-traders/blob/main/notebooks/09-matplotlib.ipynb) · [GitHub](https://github.com/quantacademyir/python-for-traders/blob/main/notebooks/09-matplotlib.ipynb) |
| 10 | [پروژه: گزارش یک‌صفحه‌ای برای یک دارایی](https://quantacademy.ir/courses/python-for-traders/project-one-page-report/) | [Colab](https://colab.research.google.com/github/quantacademyir/python-for-traders/blob/main/notebooks/10-project-one-page-report.ipynb) · [GitHub](https://github.com/quantacademyir/python-for-traders/blob/main/notebooks/10-project-one-page-report.ipynb) |

## اجرا روی کامپیوتر خودت

```sh
git clone https://github.com/quantacademyir/python-for-traders.git
cd python-for-traders
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook notebooks/
```

نوت‌بوک‌ها داده را از آدرس GitHub می‌خوانند. اگر GitHub یا اینترنت در دسترس نبود، فایل‌های پوشه `data/` را کنار نوت‌بوک بگذار و در اولین سلول `URL` را به مسیر فایل تغییر بده، مثلاً `URL = "../data/btc_daily_sample.csv"`.

## گزارش یک‌صفحه‌ای (پروژه پایانی)

```sh
python report.py data/btc_daily_sample.csv "Simulated BTC" report.png
```

فایل CSV تو باید ستون‌های `date,open,high,low,close,volume` داشته باشد.

## ساختار

| مسیر | محتوا |
|---|---|
| `notebooks/` | نوت‌بوک هر درس |
| `data/` | داده شبیه‌سازی‌شده: یک سال کندل روزانه و یک ماه کندل ساعتی با ایرادهای عمدی برای درس ۸ |
| `scripts/make_sample_data.py` | ساخت دوباره داده |
| `report.py` | پروژه پایانی به‌صورت اسکریپت |

## مجوز

کد با مجوز MIT منتشر شده است ([LICENSE](LICENSE)).

---

این repo به‌صورت خودکار از متن درس‌ها ساخته می‌شود؛ اگر اشکالی در کد دیدی، در [Issues](https://github.com/quantacademyir/python-for-traders/issues) بنویس.
