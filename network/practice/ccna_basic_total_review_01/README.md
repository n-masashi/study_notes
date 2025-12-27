## 構成の考え方
- 各グループ（企業）は独立したプライベートネットワーク
- 企業間通信はNAT後のグローバルIPを境界とする想定
- 他グループの内部ネットワークへの直接通信は行わない

## 使用している要素
- VLAN
- トランク（802.1Q）
- Inter-VLANルーティング
- OSPF
- スタティックルーティング
- NAT（PAT）
- 標準ACL

## 疎通確認
- 各グループから、他グループのNAT後グローバルIPへのping成功確認
- tracertで想定した経路を通っていることを確認

## ファイル構成
- ccna_basic_total_review_01.pkt  
  Packet Tracerファイル
- ccna_basic_total_review_01.png  
  ネットワーク構成図
- startup-config/  
  各ルータ・スイッチのstartup-config
