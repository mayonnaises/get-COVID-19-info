# Get COVID-19 Information

厚生労働省が発表している、日本国内の新型コロナウイルス感染症に関する情報を取得して、
テキスト情報として出力します。<br>
厚生労働省が更新しているCSVファイルをダウンロードすることなく、古い情報も入手することができます。
<br>
<br>
## How To Use
***Python3*** をインストール<br>

**requests** モジュールをインストール
<br>
`$ pip install requests`
<br><br>
#### 網羅的な情報を知りたい場合は、それぞれのファイルを実行してください。<br>
例：陽性者数を知りたい場合<br>
*今日・昨日・一昨日・一週間の平均・１ヶ月の平均・これまでの合計・人口に対する割合* に関する陽性者数情報が出力されます。<br>
```
$ cd number_of_cases
$ python3 get_pcr_positives.py
```
<br>

#### その他、特定の日付の情報を知りたい場合や、特定の日数前の情報を知りたい場合の関数も用意しています。<br>
例：2021年５月1日の陽性者数を知りたい場合<br>
```
>>> import get_pcr_positives as pcr
>>> pcr.get_specified_date(2021, 5, 1)
```
<br>

例：3日前の陽性者数を知りたい場合<br>
```
>>> pcr.get_minus_date(-3)
```
