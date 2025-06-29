### Docker (Compose) コマンドについて

#### 未使用のコンテナ、ネットワーク、イメージ、ボリュームをすべて削除

`docker system prune -a --volumes`

※ prune: 取り除く、刈り取る  
https://docs.docker.com/reference/cli/docker/system/prune/

---

#### コンテナを停止、up によって作成されたコンテナ、ネットワーク、ボリューム、イメージを削除

`docker compose down --remove-orphans -v`

`--remove-orphans`: Compose ファイルで定義されていないサービスのコンテナを削除  
`-v, --volumes`: Compose ファイルの "volumes" セクションで宣言された名前付きボリュームと、コンテナにアタッチされた匿名ボリュームを削除
https://docs.docker.com/reference/cli/docker/compose/down/

https://docs.docker.com/reference/cli/docker/

### マイグレーションについて

watch モードだとコンテナ → ホスト側へのファイル作成が反映されないのでマイグレーションコマンドを打ってもファイルが作成されない
バインドマウントをするしかなかった
