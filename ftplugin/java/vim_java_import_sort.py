import vim

def gen_block(prefix, imports):
  printed = False
  for package in imports:
    if package.startswith(prefix):
      vim.current.buffer.append('import {package};'.format(package=package))
      printed = True

  if printed:
    vim.current.buffer.append('')

  return filter(lambda x: not x.startswith(prefix), imports)

def sort_imports():
  imports = []
  out = []

  first_import = None
  last_import = None
  for idx, line in enumerate(vim.current.buffer):
    if line.strip().startswith('import'):
      package = line.split()[1].strip(';')
      # treat "import static" as a regular code line
      if package == 'static':
	out.append(line.rstrip('\r\n')+'\n')
	continue

      if first_import == None:
	first_import = idx

      last_import = idx
      imports.append(package)

    out.append(line.rstrip('\r\n')+'\n')

  imports.sort()

  if not first_import:
    vim.current.buffer[:] = out
    return

  vim.current.buffer[:] = out[:first_import]

  imports = gen_block('java.', imports)
  imports = gen_block('javax.', imports)
  imports = gen_block('net.', imports)
  imports = gen_block('org.', imports)
  imports = gen_block('com.', imports)
  gen_block('', imports)

  out = out[last_import+1:]
  while len(out[0].strip()) < 1:
    out.pop(0)

  vim.current.buffer.append(out)

def main():
  cursor = vim.current.window.cursor
  sort_imports()
  vim.current.window.cursor = cursor
