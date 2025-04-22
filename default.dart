{
    "machine": {
        "gpu": 0,
        "ram": 400,
        "cpu": 400,
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
                "Image": "ghcr.io/darts2024/nearai:{{ or .dockerTag "v0.1.0"}}",
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
                "Memory": "{{(or .ram "400")}}",
                "CPU": "{{ or .cpu "400" }}"
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
