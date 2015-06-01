" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! JavaImportSort()
python << endOfPython

import vim_java_import_sort
vim_java_import_sort.main()

endOfPython
endfunction

" --------------------------------
"  Sort automatically on read and write
" --------------------------------
au BufWritePre,BufRead *.java call JavaImportSort()
