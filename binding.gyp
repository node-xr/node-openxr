{
  'variables': {
    'platform': '<(OS)',
  },
  'conditions': [
    ['platform == "mac"', {'variables': {'platform': 'darwin'}}],
    ['platform == "win"', {'variables': {'platform': 'win32'}}],
  ],
  'targets': [
    {
      'target_name': 'openxr',
      'defines': [
        'NAPI_VERSION=3',
      ],
      'sources': [
        'src/bindings.cpp',
        'src/sdl/events.cpp',
        'src/sdl/quit.cpp',
        'src/sdl/sdl.cpp',
        'src/sdl/syswm.cpp',
        'src/sdl/video.cpp',
        'src/util.cpp',
      ],
      'include_dirs': [
        '<(module_root_dir)/deps/sdl2/include',
      ],
      'conditions': [
        ['platform=="linux"', {
          'library_dirs': ['<(module_root_dir)/deps/sdl2/lib/linux/x64'],
          'libraries': [
            '-Wl,-rpath,<(module_root_dir)/deps/sdl2/lib/linux/x64',
            '<(module_root_dir)/deps/sdl2/lib/linux/x64/libSDL2-2.0.so.0'
          ],
        }],
        ['platform=="darwin"', {
          'library_dirs': ['<(module_root_dir)/deps/sdl2/lib/darwin/x64'],
          'libraries': [
            '-Wl,-rpath,<(module_root_dir)/deps/sdl2/lib/darwin/x64',
            '<(module_root_dir)/deps/sdl2/lib/darwin/x64/SDL2.dylib'
          ],
        }],
        ['platform=="win32"', {
          'library_dirs': ['<(module_root_dir)/deps/sdl2/lib/win32/x64'],
          'libraries': ['SDL2.lib'],
          'defines' : ['WIN32_LEAN_AND_MEAN', 'VC_EXTRALEAN', 'NOMINMAX'],
          'msvs_settings' : {
            'VCCLCompilerTool' : {
              'AdditionalOptions' : ['/O2','/Oy','/GL','/GF','/Gm-','/EHsc','/MT','/GS','/Gy','/GR-','/Gd']
            },
            'VCLinkerTool' : {
              'AdditionalOptions' : ['/OPT:REF','/OPT:ICF','/LTCG']
            },
          },
          'copies':
          [
            {
              'destination': '<(module_root_dir)/build/Release',
              'files': ['<(module_root_dir)/deps/sdl2/lib/win32/x64/SDL2.dll']
            }
          ],
        }],
      ],
    }
  ]
}