# ship-display
1.在ship-main.py的ship_list中按示例格式填入跑船兄弟的姓名和船舶IMO号(注意不是mmsi号) 2.在index.html中，在ship_list中有几个室友,就复制粘贴几个室友function(),并将每个的function()的shipNumber按顺序改好 3.将项目的三个文件部署到服务器即可

注意：部署后,ship-main.py必须保持后台运行才能实时显示船舶位置,linux平台下可用命令nuhop

```
nohup python ship-main.py &
```

