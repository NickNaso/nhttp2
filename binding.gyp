{
    'variables': {
    },
    'targets': [
        {
            'target_name': 'nhttp2',
            'dependencies': [
                'src/deps/nghttp2/nghttp2.gyp:nghttp2'
            ],
            'cflags': [
                
            ],
            'defines': [
                
            ],
            'include_dirs': [
                "<!(node -e \"require('nan')\")"
            ],
            'sources': [
                'src/nhttp2.cc',
            ],
            'link_settings': {
                'ldflags': [
                ],
                'libraries': [
                ]
            }
        }
    ]
}
