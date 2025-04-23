{
    "machine": {
        "gpu": 0,
        "ram": {{ mul (regex "\\d+" (or .ram "1gb")) 1000 }},
        "cpu": 500
    },
    "job": {
        "APIVersion": "V1beta1",
        "Spec": {
            "Deal": {
                "Concurrency": 1
            },
           "Docker": {
                "Entrypoint": [
                    "bun", "start", "generate"
                ],
                "Image": "ghcr.io/darts2024/nearai:{{ or .dockerTag "v0.1.3"}}",
                "EnvironmentVariables": [
                    {{if .Prompt}}"{{ subt "PROMPT=%s" .Prompt }}"{{else}}"PROMPT=A whimsical forest creature with oversized ears and a mischievous grin, surrounded by glowing fireflies"{{end}},
                    "OUTPUT_DIR=/outputs/",
                    "HF_HUB_OFFLINE=1"
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
                "CPU": "{{ or .cpu "500m" }}"
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
