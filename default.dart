{
    "machine": {
        "gpu": 0,
        "ram": {{ mul (regex "\\d+" (or .ram "1gb")) 1000 }},
        "cpu": {{ mul (or .cpu "1") 1000 }}
    },
    "job": {
        "APIVersion": "V1beta1",
        "Spec": {
            "Deal": {
                "Concurrency": 1
            },
           "Docker": {
                "Entrypoint": [
                    "bun", "start", "{{(or .Cmd "generate")}}"
                ],
                "Image": "ghcr.io/darts2024/nearai:{{ or .dockerTag "v0.3.1"}}",
                "EnvironmentVariables": [
                    {{if .Prompt}}"{{ subt "PROMPT=%s" .Prompt }}"{{else}}"PROMPT=A whimsical forest creature with oversized ears and a mischievous grin, surrounded by glowing fireflies"{{end}},
                    "OUTPUT_DIR=/outputs/",
                    "{{ subt "NUM_IMAGES=%s" (or .N "1")  }}",
                    "{{ subt "RANDOM_SEED=%s" (or .Seed "1")  }}"
                ]
            },
            "Engine": "Docker",
            "Language": {
                "JobContext": {}
            },
            "Network": {
                "Type": "Full"
            },
            "PublisherSpec": {
                "Type": "local"
            },
            "Resources": {
                "Memory": "{{(or .ram "1gb")}}",
                "CPU": "{{ or .cpu "1" }}"
           },
            "Timeout": 1800,
            "Verifier": "Noop",
            "Wasm": {
                "EntryModule": {}
            },
            "outputs": [
                {
                    "Name": "outputs",
                    "path" :"/outputs"
                }
            ]
        }
    }
}
