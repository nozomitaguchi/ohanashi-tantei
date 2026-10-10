# おはなし探偵
小１程度の文章題12問。ビルド不要の静的サイトです。

## GitHub Pages
このフォルダの index.html / style.css / app.js と audio フォルダをリポジトリ直下へ追加します。
GitHub の Settings → Pages → Deploy from a branch → main / (root) → Save を選択します。
公開URLはPages画面に表示されます。サブパスにも対応しています。

音声はGoogle AI StudioのGeminiで生成した12問分のWAVを再生します。公開サイトでAPIキーは不要です。文章を変更した場合は対応する音声も作り直してください。
Google Fontsが利用できない場合は端末のフォントで表示します。
記録はlocalStorageに保存。サーバーへの成績送信はありません。

## 学習の流れ
何を求めるかを選ぶ → 数字と＋・−で式を組み立てる → 答えを出す。足し算は数の順序を入れ替えても正解です。

文章は場面説明・不要な数・時間の順序を含むオリジナル問題へ調整。３問は３つの数の式に対応しています。
