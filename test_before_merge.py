#!/usr/bin/env python
"""Quick test to verify the fix works"""
import sys
import os

os.chdir('e:\\03_Projects\\Python-Ytdownloader.worktrees\\agents-fix-ui-form-attribute-error')

print("Testing if the AttributeError is fixed...\n")

try:
    # This is what main.py does on line 12-19
    from Youtube_Downloader_ui import Ui_Form
    from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
    
    app = QApplication([])
    central_widget = QWidget()
    ui = Ui_Form()
    ui.setupUi(central_widget)
    
    # Line 19 of main.py - this was failing before
    print("✓ Created UI successfully")
    print("✓ Accessing searchButton:", hasattr(ui, 'searchButton'))
    print("✓ Accessing label_image:", hasattr(ui, 'label_image'))
    
    # Try the connection that was failing
    ui.searchButton.clicked.connect(lambda: None)
    print("✓ Signal connection works\n")
    
    print("=" * 50)
    print("✅ FIX VERIFIED - No AttributeError!")
    print("=" * 50)
    print("\nNext steps:")
    print("1. Run: python _cleanup_script.py")
    print("2. Commit changes")
    print("3. Merge to main branch")
    
except AttributeError as e:
    print(f"❌ ERROR: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
