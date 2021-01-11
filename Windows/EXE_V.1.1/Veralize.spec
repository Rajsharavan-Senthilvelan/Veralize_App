# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Veralize.py'],
             pathex=['C:\\Users\\us121\\Desktop\\Raj'],
             binaries=[],
             datas=[('beep.wav', '.'), ('1215email.png', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Veralize',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='v.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Veralize')
