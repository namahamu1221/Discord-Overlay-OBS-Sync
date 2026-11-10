# Discord Overlay OBS URL Sync

Discord-Overlay が変更した Discord StreamKit のブラウザソース URL を、OBS Studio 内の別のブラウザソースへ自動同期する Python スクリプトです。

立ち絵用と VC 表示用など、**異なるカスタム CSS を保持したまま**同じ VC の URL を使えます。

> 非公式の補助スクリプトです。Discord、OBS Studio、および Discord-Overlay の公式製品ではありません。

## 機能

- 同期元ブラウザソースの URL を 500 ミリ秒ごとに確認
- URL が変わったときだけ同期先ブラウザソースを更新
- URL 以外の設定（カスタム CSS 等）は変更しない
- 同期元・同期先の名前を OBS のスクリプト設定画面で指定可能
- 外部 Python パッケージ不要（OBS の `obspython` API を使用）

## 必要なもの

- OBS Studio（Python スクリプト対応版）
- OBS がサポートする Python のインストール・設定
- OBS に作成した**独立した**ブラウザソース 2 個（「参照」ではなく、それぞれ新規作成）
- [Discord-Overlay（Kenshin9977）](https://github.com/Kenshin9977/Discord-Overlay/)（同期元の URL を自動更新するため。独立した別プロジェクト）

## 使い方

1. OBS で 2 つのブラウザソースをそれぞれ「新規作成」する（例：`Discord-Overlay` と `Discord-VC`）。
2. 2 つのソースにそれぞれ必要なカスタム CSS を設定する。
3. Discord-Overlay 側で **同期元**のブラウザソースを更新するよう設定する。
4. OBS の **ツール → スクリプト → Python の設定** で、対応する Python を指定する。
5. **スクリプト** の `+` ボタンから `discord_overlay_url_sync.py` を追加する。
6. 「同期元のブラウザソース名」と「同期先のブラウザソース名」に、OBS での正確なソース名を入力する。
7. Discord の VC を移動し、両方の URL が更新されることを確認する。

### 設定例

| 項目 | 値 |
| --- | --- |
| 同期元のブラウザソース名 | `Discord-Overlay` |
| 同期先のブラウザソース名 | `Discord-VC` |

## 注意事項

- このバージョンは **1 対 1 の URL 同期**のみ対応します。
- CSS の貼り付け・保存・自動切り替えには**対応していません**。それぞれのブラウザソースの CSS は OBS 側で編集してください。
- URL が空の場合、同期されません。
- ソース名が一致しない、またはソースがブラウザソースでない場合、同期しません。
- URL が同じでも同期先の設定を変更した場合、次に同期元の URL が変化するまで上書きされません。
- 実際の OBS 環境での動作確認は各自の環境で行ってください。

## 関連プロジェクト

- **[Kenshin9977/Discord-Overlay](https://github.com/Kenshin9977/Discord-Overlay/)** — Discord の VC 移動に応じて OBS の StreamKit ブラウザソース URL を更新するツール。

本スクリプトは、このツールが更新した URL を別のブラウザソースにも同期するための**非公式・独立した補助ツール**です。Discord-Overlay の開発元による公式の拡張機能ではありません。

## ライセンス

MIT License。詳細は [LICENSE](LICENSE) を参照してください。
