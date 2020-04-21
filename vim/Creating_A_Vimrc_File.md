# Creating a Vimrc file

A vimrc file is a set of commands that run whenever vim is launched, used to customize your default vim session. On windows, this needs to be placed in your user directory, so for me, this was: 

```
C:\Users\Kyle Halladay\.vimrc
```

Currently, the contents of my vimrc file are as follows: 

```
" Enable syntax highlighting
syntax on

" Add line numbers
set number

" Set Color Scheme
colorscheme industry

" Disable bell sounds 
set noerrorbells visualbell t_vb=

" Make tabs not stupid big and set things up for the autoindent
set expandtab
set tabstop=2
set shiftwidth=2
set autoindent
set smartindent

" Remap esc to jk
:imap jk <Esc>
```