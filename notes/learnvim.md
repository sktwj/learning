1. 在任意系统中，在Vim中执行:echo $MYVIMRC命令可以快速得知这个文件的位置和名称。 文件的路径会在屏幕的底部显示。
2. imap <c-d> <esc>ddi   在insert模式中做dd操作
3. 每一个*map系列的命令都有个对应的*noremap命令，包括：noremap/nnoremap、 vnoremap和inoremap。这些命令将不递归解释映射的内容。 该何时使用这些非递归的映射命令呢？ 答案是： 任何时候 。 是的, 没开玩笑， 任何时候 。
4. VIM 可以映射多个按键
:nnoremap -d dd            删除一行
:nnoremap -c ddO           删除一行并进入insert模式
5. 设置leader键        :let mapleader = ","
6. 设置local leader    :let maplocalleader = "\\"  用于 只对某些文件而设置的映射
7. nnoremap <leader>ev :vsplit $MYVIMRC<cr>
8. nnoremap <leader>sv :"source" $MYVIMRC<cr>
9. :iabbrev ssig -- <cr>Steve Losh<cr>steve@stevelosh.com    缩略词
10. :nnoremap <leader>" viw<esc>a"<esc>hbi"<esc>lel  双引号包围单词
11. autocmd BufferNewFile \****.txt :write
12.:autocmd BufNewFile,BufRead *.html setlocal nowrap   上面的命令会使得无论你在什么时候编辑HTML文件自动换行都会被关闭。
13. :autocmd FileType javascript nnoremap <buffer> <localleader>c I//<esc>
:autocmd FileType python     nnoremap <buffer> <localleader>c I#<esc>
根据js和python类型打开时候 做注释快捷映射
:autocmd FileType python     :iabbrev <buffer> iff if:<left>
:autocmd FileType javascript :iabbrev <buffer> iff if ()<left>
小型 snippet
14. :augroup testgroup    命令组
:    autocmd!     自动清理前命令
:    autocmd BufWrite * :echom "Cats"
:augroup END

15. ci(     修改   在括号内
    yt,     复制    到逗号
