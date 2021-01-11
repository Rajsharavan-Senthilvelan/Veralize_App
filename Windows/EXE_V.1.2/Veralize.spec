# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Veralize.py'],
             pathex=['C:\\Users\\us121\\Desktop\\Raj\\Veralize_V_1.2\\EXE_V.1.2'],
             binaries=[],
             datas=[('beep.wav', '.'), ('veralize_logo.png', '.'), ('logo.PNG', '.'), ('key.txt', '.'), ('encrypted', '.')],
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
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Veralize')
