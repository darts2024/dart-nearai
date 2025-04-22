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
                    "bun", "start", "generate"
                ],
                "Image": "ghcr.io/darts2024/nearai:{{ or .dockerTag "v0.1.1"}}",
                "EnvironmentVariables": [
                    {{if .Prompt}}"{{ subt "PROMPT=%s" .Prompt }}"{{else}}"PROMPT="{{end}},
                    "OUTPUT_DIR=/outputs/",
                    "HF_HUB_OFFLINE=1"
                ]
            },
            "Engine": "Docker",
            "Language": {
                "JobContext": {}
            },
            "Network": {
                "Type": "None"
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
