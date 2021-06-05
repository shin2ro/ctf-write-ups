# git-leak

> 後輩が誤って機密情報をコミットしてしまったらしいです。ひとまずコミットを上書きして消したからこれで大丈夫ですよね？

## Write-up

```
$ git reflog
e0b545f (HEAD -> master) HEAD@{0}: commit (amend): feat: めもを追加
80f3044 HEAD@{1}: commit (amend): feat: めもを追加
b3bfb5c HEAD@{2}: rebase -i (finish): returning to refs/heads/master
b3bfb5c HEAD@{3}: commit (amend): feat: めもを追加
7387982 HEAD@{4}: rebase -i: fast-forward
36a4809 HEAD@{5}: rebase -i (start): checkout HEAD~2
7387982 HEAD@{6}: reset: moving to HEAD
7387982 HEAD@{7}: commit: feat: めもを追加
36a4809 HEAD@{8}: commit: feat: commit-treeの説明を追加
9ac9b0c HEAD@{9}: commit: change: 順番を変更
8fc078d HEAD@{10}: commit: feat: git cat-fileの説明を追加
d3b47fe HEAD@{11}: commit: feat: fsckを追記する
f66de64 HEAD@{12}: commit: feat: reflogの説明追加
d5aeffe HEAD@{13}: commit: feat: resetの説明を追加
a4f7fe9 HEAD@{14}: commit: feat: git logの説明を追加
9fcb006 HEAD@{15}: commit: feat: git commitの説明追加
6d21e22 HEAD@{16}: commit: feat: git addの説明を追加
656db59 HEAD@{17}: commit: feat: add README.md
c27f346 HEAD@{18}: commit (initial): initial commit
```

`reset`してる前のハッシュをチェックアウトします。

```
$ git checkout 7387982
$ cat flag.txt
```

## Flag

`ctf4b{0verwr1te_1s_n0t_c0mplete_1n_G1t}`
