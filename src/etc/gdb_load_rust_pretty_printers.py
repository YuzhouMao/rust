import gdb_rust_pretty_printing
gdb_rust_pretty_printing.register_printers(gdb.current_objfile())
