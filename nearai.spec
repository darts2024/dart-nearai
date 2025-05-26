{
  "openapi": "3.1.0",
  "info": {
    "title": "FastAPI",
    "version": "0.1.0"
  },
  "paths": {
    "/v1/completions": {
      "post": {
        "summary": "Completions",
        "operationId": "completions_v1_completions_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "anyOf": [
                  {
                    "$ref": "#/components/schemas/ChatCompletionsRequest"
                  },
                  {
                    "$ref": "#/components/schemas/CompletionsRequest"
                  },
                  {
                    "$ref": "#/components/schemas/EmbeddingsRequest"
                  },
                  {
                    "$ref": "#/components/schemas/ImageGenerationRequest"
                  }
                ],
                "title": "Request"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/get_agent_public_key": {
      "post": {
        "summary": "Get Agent Public Key",
        "operationId": "get_agent_public_key_v1_get_agent_public_key_post",
        "parameters": [
          {
            "name": "agent_name",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Agent Name"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/chat/completions": {
      "post": {
        "summary": "Chat Completions",
        "operationId": "chat_completions_v1_chat_completions_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "anyOf": [
                  {
                    "$ref": "#/components/schemas/ChatCompletionsRequest"
                  },
                  {
                    "$ref": "#/components/schemas/CompletionsRequest"
                  },
                  {
                    "$ref": "#/components/schemas/EmbeddingsRequest"
                  },
                  {
                    "$ref": "#/components/schemas/ImageGenerationRequest"
                  }
                ],
                "title": "Request"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/models": {
      "get": {
        "summary": "Get Models",
        "operationId": "get_models_v1_models_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        }
      }
    },
    "/v1/embeddings": {
      "post": {
        "summary": "Embeddings",
        "operationId": "embeddings_v1_embeddings_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "anyOf": [
                  {
                    "$ref": "#/components/schemas/ChatCompletionsRequest"
                  },
                  {
                    "$ref": "#/components/schemas/CompletionsRequest"
                  },
                  {
                    "$ref": "#/components/schemas/EmbeddingsRequest"
                  },
                  {
                    "$ref": "#/components/schemas/ImageGenerationRequest"
                  }
                ],
                "title": "Request"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/nonce/revoke": {
      "post": {
        "summary": "Revoke Nonce",
        "description": "Revoke a nonce for the account.",
        "operationId": "revoke_nonce_v1_nonce_revoke_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RevokeNonce"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/nonce/revoke/all": {
      "post": {
        "summary": "Revoke All Nonces",
        "description": "Revoke all nonces for the account.",
        "operationId": "revoke_all_nonces_v1_nonce_revoke_all_post",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/nonce/list": {
      "get": {
        "summary": "List Nonces",
        "description": "List all nonces for the account.",
        "operationId": "list_nonces_v1_nonce_list_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/version": {
      "get": {
        "summary": "Version",
        "operationId": "version_v1_version_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "string",
                  "title": "Response Version V1 Version Get"
                }
              }
            }
          }
        }
      }
    },
    "/v1/images/generations": {
      "post": {
        "summary": "Generate Images",
        "operationId": "generate_images_v1_images_generations_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "anyOf": [
                  {
                    "$ref": "#/components/schemas/ChatCompletionsRequest"
                  },
                  {
                    "$ref": "#/components/schemas/CompletionsRequest"
                  },
                  {
                    "$ref": "#/components/schemas/EmbeddingsRequest"
                  },
                  {
                    "$ref": "#/components/schemas/ImageGenerationRequest"
                  }
                ],
                "title": "Request"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/registry/upload_file": {
      "post": {
        "tags": [
          "registry"
        ],
        "summary": "Upload File",
        "operationId": "upload_file_v1_registry_upload_file_post",
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Body_upload_file_v1_registry_upload_file_post"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/registry/download_file": {
      "post": {
        "tags": [
          "registry"
        ],
        "summary": "Download File",
        "operationId": "download_file_v1_registry_download_file_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Body_download_file_v1_registry_download_file_post"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/registry/upload_metadata": {
      "post": {
        "tags": [
          "registry"
        ],
        "summary": "Upload Metadata",
        "operationId": "upload_metadata_v1_registry_upload_metadata_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Body_upload_metadata_v1_registry_upload_metadata_post"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/registry/download_metadata": {
      "post": {
        "tags": [
          "registry"
        ],
        "summary": "Download Metadata",
        "operationId": "download_metadata_v1_registry_download_metadata_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Body_download_metadata_v1_registry_download_metadata_post"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/EntryMetadata"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/registry/list_files": {
      "post": {
        "tags": [
          "registry"
        ],
        "summary": "List Files",
        "description": "Lists all files that belong to an entry.",
        "operationId": "list_files_v1_registry_list_files_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Body_list_files_v1_registry_list_files_post"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "items": {
                    "$ref": "#/components/schemas/Filename"
                  },
                  "type": "array",
                  "title": "Response List Files V1 Registry List Files Post"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/registry/list_entries": {
      "post": {
        "tags": [
          "registry"
        ],
        "summary": "List Entries",
        "operationId": "list_entries_v1_registry_list_entries_post",
        "parameters": [
          {
            "name": "namespace",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "default": "",
              "title": "Namespace"
            }
          },
          {
            "name": "category",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "default": "",
              "title": "Category"
            }
          },
          {
            "name": "tags",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "default": "",
              "title": "Tags"
            }
          },
          {
            "name": "total",
            "in": "query",
            "required": false,
            "schema": {
              "type": "integer",
              "default": 32,
              "title": "Total"
            }
          },
          {
            "name": "offset",
            "in": "query",
            "required": false,
            "schema": {
              "type": "integer",
              "default": 0,
              "title": "Offset"
            }
          },
          {
            "name": "show_hidden",
            "in": "query",
            "required": false,
            "schema": {
              "type": "boolean",
              "default": false,
              "title": "Show Hidden"
            }
          },
          {
            "name": "show_latest_version",
            "in": "query",
            "required": false,
            "schema": {
              "type": "boolean",
              "default": true,
              "title": "Show Latest Version"
            }
          },
          {
            "name": "starred_by",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "default": "",
              "title": "Starred By"
            }
          },
          {
            "name": "star_point_of_view",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "default": "",
              "title": "Star Point Of View"
            }
          },
          {
            "name": "fork_of_name",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "default": "",
              "title": "Fork Of Name"
            }
          },
          {
            "name": "fork_of_namespace",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "default": "",
              "title": "Fork Of Namespace"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/EntryInformation"
                  },
                  "title": "Response List Entries V1 Registry List Entries Post"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/registry/fork": {
      "post": {
        "tags": [
          "registry"
        ],
        "summary": "Fork Entry",
        "description": "Fork an existing registry entry to the current user's namespace.",
        "operationId": "fork_entry_v1_registry_fork_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Body_fork_entry_v1_registry_fork_post"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ForkResult"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/agent/runs": {
      "post": {
        "tags": [
          "agents, assistants",
          "Agents",
          "Assistants"
        ],
        "summary": "Run Agent",
        "description": "Run an agent against an existing or a new thread.\n\nReturns the ID of the new thread resulting from the run.",
        "operationId": "run_agent_v1_agent_runs_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateThreadAndRunRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "string",
                  "title": "Response Run Agent V1 Agent Runs Post"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/threads/runs": {
      "post": {
        "tags": [
          "agents, assistants",
          "Agents",
          "Assistants"
        ],
        "summary": "Run Agent",
        "description": "Run an agent against an existing or a new thread.\n\nReturns the ID of the new thread resulting from the run.",
        "operationId": "run_agent_v1_threads_runs_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateThreadAndRunRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "string",
                  "title": "Response Run Agent V1 Threads Runs Post"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/find_agents": {
      "post": {
        "tags": [
          "agents, assistants"
        ],
        "summary": "Find Agents",
        "description": "Find agents based on various parameters.",
        "operationId": "find_agents_v1_find_agents_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/FilterAgentsRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "items": {
                    "$ref": "#/components/schemas/RegistryEntry"
                  },
                  "type": "array",
                  "title": "Response Find Agents V1 Find Agents Post"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/agent_data": {
      "get": {
        "tags": [
          "agents, assistants"
        ],
        "summary": "Get Agent Data",
        "operationId": "get_agent_data_v1_agent_data_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "items": {
                    "$ref": "#/components/schemas/AgentData"
                  },
                  "type": "array",
                  "title": "Response Get Agent Data V1 Agent Data Get"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      },
      "post": {
        "tags": [
          "agents, assistants"
        ],
        "summary": "Save Agent Data",
        "operationId": "save_agent_data_v1_agent_data_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/AgentDataRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/AgentData"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/agent_data/{key}": {
      "get": {
        "tags": [
          "agents, assistants"
        ],
        "summary": "Get Agent Data By Key",
        "operationId": "get_agent_data_by_key_v1_agent_data__key__get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "key",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Key"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "anyOf": [
                    {
                      "$ref": "#/components/schemas/AgentData"
                    },
                    {
                      "type": "null"
                    }
                  ],
                  "title": "Response Get Agent Data By Key V1 Agent Data  Key  Get"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/agent_data_admin/{namespace}/{name}": {
      "get": {
        "tags": [
          "agents, assistants"
        ],
        "summary": "Get Agent Data For Author",
        "operationId": "get_agent_data_for_author_v1_agent_data_admin__namespace___name__get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "namespace",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Namespace"
            }
          },
          {
            "name": "name",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Name"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/AgentData"
                  },
                  "title": "Response Get Agent Data For Author V1 Agent Data Admin  Namespace   Name  Get"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/agent_data_admin/{namespace}/{name}/{key}": {
      "get": {
        "tags": [
          "agents, assistants"
        ],
        "summary": "Get Agent Data By Key For Author",
        "operationId": "get_agent_data_by_key_for_author_v1_agent_data_admin__namespace___name___key__get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "namespace",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Namespace"
            }
          },
          {
            "name": "name",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Name"
            }
          },
          {
            "name": "key",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Key"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "anyOf": [
                    {
                      "$ref": "#/components/schemas/AgentData"
                    },
                    {
                      "type": "null"
                    }
                  ],
                  "title": "Response Get Agent Data By Key For Author V1 Agent Data Admin  Namespace   Name   Key  Get"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/benchmark/create": {
      "get": {
        "tags": [
          "benchmark"
        ],
        "summary": "Create Benchmark",
        "operationId": "create_benchmark_v1_benchmark_create_get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "benchmark_name",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Benchmark Name"
            }
          },
          {
            "name": "solver_name",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Solver Name"
            }
          },
          {
            "name": "solver_args",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Solver Args"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "integer",
                  "title": "Response Create Benchmark V1 Benchmark Create Get"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/benchmark/get": {
      "get": {
        "tags": [
          "benchmark"
        ],
        "summary": "Get Benchmark",
        "description": "Get the ID of a benchmark given its attributes.\n\nReturn -1 if the benchmark does not exist.",
        "operationId": "get_benchmark_v1_benchmark_get_get",
        "parameters": [
          {
            "name": "namespace",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Namespace"
            }
          },
          {
            "name": "benchmark_name",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Benchmark Name"
            }
          },
          {
            "name": "solver_name",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Solver Name"
            }
          },
          {
            "name": "solver_args",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Solver Args"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "integer",
                  "title": "Response Get Benchmark V1 Benchmark Get Get"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/benchmark/list": {
      "get": {
        "tags": [
          "benchmark"
        ],
        "summary": "List Benchmarks",
        "operationId": "list_benchmarks_v1_benchmark_list_get",
        "parameters": [
          {
            "name": "namespace",
            "in": "query",
            "required": false,
            "schema": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ],
              "title": "Namespace"
            }
          },
          {
            "name": "benchmark_name",
            "in": "query",
            "required": false,
            "schema": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ],
              "title": "Benchmark Name"
            }
          },
          {
            "name": "solver_name",
            "in": "query",
            "required": false,
            "schema": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ],
              "title": "Solver Name"
            }
          },
          {
            "name": "solver_args",
            "in": "query",
            "required": false,
            "schema": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ],
              "title": "Solver Args"
            }
          },
          {
            "name": "total",
            "in": "query",
            "required": false,
            "schema": {
              "type": "integer",
              "default": 32,
              "title": "Total"
            }
          },
          {
            "name": "offset",
            "in": "query",
            "required": false,
            "schema": {
              "type": "integer",
              "default": 0,
              "title": "Offset"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/BenchmarkOutput"
                  },
                  "title": "Response List Benchmarks V1 Benchmark List Get"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/benchmark/add_result": {
      "get": {
        "tags": [
          "benchmark"
        ],
        "summary": "Add Benchmark Result",
        "operationId": "add_benchmark_result_v1_benchmark_add_result_get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "benchmark_id",
            "in": "query",
            "required": true,
            "schema": {
              "type": "integer",
              "title": "Benchmark Id"
            }
          },
          {
            "name": "index",
            "in": "query",
            "required": true,
            "schema": {
              "type": "integer",
              "title": "Index"
            }
          },
          {
            "name": "solved",
            "in": "query",
            "required": true,
            "schema": {
              "type": "boolean",
              "title": "Solved"
            }
          },
          {
            "name": "info",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Info"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/benchmark/get_result": {
      "get": {
        "tags": [
          "benchmark"
        ],
        "summary": "Get Benchmark Result",
        "operationId": "get_benchmark_result_v1_benchmark_get_result_get",
        "parameters": [
          {
            "name": "benchmark_id",
            "in": "query",
            "required": true,
            "schema": {
              "type": "integer",
              "title": "Benchmark Id"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/BenchmarkResultOutput"
                  },
                  "title": "Response Get Benchmark Result V1 Benchmark Get Result Get"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/stars/add_star": {
      "post": {
        "tags": [
          "stars"
        ],
        "summary": "Add Star",
        "operationId": "add_star_v1_stars_add_star_post",
        "requestBody": {
          "content": {
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Body_add_star_v1_stars_add_star_post"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/stars/remove_star": {
      "post": {
        "tags": [
          "stars"
        ],
        "summary": "Remove Star",
        "operationId": "remove_star_v1_stars_remove_star_post",
        "requestBody": {
          "content": {
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Body_remove_star_v1_stars_remove_star_post"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/jobs/add_job": {
      "post": {
        "tags": [
          "jobs"
        ],
        "summary": "Add Job",
        "operationId": "add_job_v1_jobs_add_job_post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "worker_kind",
            "in": "query",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/WorkerKind"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Body_add_job_v1_jobs_add_job_post"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Job"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/jobs/get_pending_job": {
      "post": {
        "tags": [
          "jobs"
        ],
        "summary": "Get Pending Job",
        "operationId": "get_pending_job_v1_jobs_get_pending_job_post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "worker_id",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Worker Id"
            }
          },
          {
            "name": "worker_kind",
            "in": "query",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/WorkerKind"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SelectedJob"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/jobs/list_jobs": {
      "get": {
        "tags": [
          "jobs"
        ],
        "summary": "List Jobs",
        "operationId": "list_jobs_v1_jobs_list_jobs_get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "account_id",
            "in": "query",
            "required": true,
            "schema": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ],
              "title": "Account Id"
            }
          },
          {
            "name": "status",
            "in": "query",
            "required": true,
            "schema": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/JobStatus"
                },
                {
                  "type": "null"
                }
              ],
              "title": "Status"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Job"
                  },
                  "title": "Response List Jobs V1 Jobs List Jobs Get"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/jobs/update_job": {
      "post": {
        "tags": [
          "jobs"
        ],
        "summary": "Update Job",
        "operationId": "update_job_v1_jobs_update_job_post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "job_id",
            "in": "query",
            "required": true,
            "schema": {
              "type": "integer",
              "title": "Job Id"
            }
          },
          {
            "name": "status",
            "in": "query",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/JobStatus"
            }
          },
          {
            "name": "result_json",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "default": "",
              "title": "Result Json"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/permissions/grant_permission": {
      "post": {
        "tags": [
          "permissions"
        ],
        "summary": "Grant Permission",
        "operationId": "grant_permission_v1_permissions_grant_permission_post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "account_id",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "default": "",
              "title": "Account Id"
            }
          },
          {
            "name": "permission",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "default": "",
              "title": "Permission"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/permissions/revoke_permission": {
      "post": {
        "tags": [
          "permissions"
        ],
        "summary": "Revoke Permission",
        "operationId": "revoke_permission_v1_permissions_revoke_permission_post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "account_id",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "default": "",
              "title": "Account Id"
            }
          },
          {
            "name": "permission",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "default": "",
              "title": "Permission"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/evaluation/table": {
      "get": {
        "tags": [
          "evaluation"
        ],
        "summary": "Table",
        "operationId": "table_v1_evaluation_table_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/EvaluationTable"
                }
              }
            }
          }
        }
      }
    },
    "/v1/delegation/delegate": {
      "post": {
        "tags": [
          "delegation"
        ],
        "summary": "Delegate",
        "operationId": "delegate_v1_delegation_delegate_post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "delegate_account_id",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Delegate Account Id"
            }
          },
          {
            "name": "expires_at",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "format": "date-time",
              "title": "Expires At"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/delegation/list_delegations": {
      "post": {
        "tags": [
          "delegation"
        ],
        "summary": "List Delegation",
        "operationId": "list_delegation_v1_delegation_list_delegations_post",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "items": {
                    "$ref": "#/components/schemas/Delegation"
                  },
                  "type": "array",
                  "title": "Response List Delegation V1 Delegation List Delegations Post"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/delegation/revoke_delegation": {
      "post": {
        "tags": [
          "delegation"
        ],
        "summary": "Revoke Delegation",
        "operationId": "revoke_delegation_v1_delegation_revoke_delegation_post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "delegate_account_id",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Delegate Account Id"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/logs/add_log": {
      "post": {
        "tags": [
          "logs"
        ],
        "summary": "Add Log",
        "operationId": "add_log_v1_logs_add_log_post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "target",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Target"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "title": "Info"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Log"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/logs/get_logs": {
      "get": {
        "tags": [
          "logs"
        ],
        "summary": "Get Logs",
        "operationId": "get_logs_v1_logs_get_logs_get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "target",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Target"
            }
          },
          {
            "name": "after_id",
            "in": "query",
            "required": true,
            "schema": {
              "type": "integer",
              "title": "After Id"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "required": true,
            "schema": {
              "type": "integer",
              "title": "Limit"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Log"
                  },
                  "title": "Response Get Logs V1 Logs Get Logs Get"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/vector_stores": {
      "get": {
        "tags": [
          "Vector Stores"
        ],
        "summary": "List Vector Stores",
        "description": "List all vector stores for the authenticated account.\n\nArgs:\n----\n    auth (AuthToken): The authentication token.\n\nReturns:\n-------\n    List[VectorStore]: A list of vector stores.",
        "operationId": "list_vector_stores_v1_vector_stores_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      },
      "post": {
        "tags": [
          "Vector Stores"
        ],
        "summary": "Create Vector Store",
        "description": "Create a new vector store.\n\nArgs:\n----\n    request (CreateVectorStoreRequest): The request containing vector store details.\n    background_tasks (BackgroundTasks): FastAPI background tasks.\n    auth (AuthToken): The authentication token.\n\nReturns:\n-------\n    VectorStore: The created vector store object.\n\nRaises:\n------\n    HTTPException: If the vector store creation fails.",
        "operationId": "create_vector_store_v1_vector_stores_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateVectorStoreRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/VectorStore"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      },
      "patch": {
        "tags": [
          "Vector Stores"
        ],
        "summary": "Update Vector Store",
        "description": "Update a vector store. (Not implemented).\n\nThis endpoint is a placeholder for future implementation.",
        "operationId": "update_vector_store_v1_vector_stores_patch",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        }
      }
    },
    "/v1/vector_stores/{vector_store_id}": {
      "get": {
        "tags": [
          "Vector Stores"
        ],
        "summary": "Get Vector Store",
        "description": "Retrieve a specific vector store.\n\nArgs:\n----\n    vector_store_id (str): The ID of the vector store to retrieve.\n    auth (AuthToken): The authentication token.\n\nReturns:\n-------\n    VectorStore: The requested vector store.\n\nRaises:\n------\n    HTTPException: If the vector store is not found.",
        "operationId": "get_vector_store_v1_vector_stores__vector_store_id__get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "vector_store_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Vector Store Id"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Vector Stores"
        ],
        "summary": "Delete Vector Store",
        "description": "Delete a vector store.\n\nArgs:\n----\n    vector_store_id (str): The ID of the vector store to delete.\n    auth (AuthToken): The authentication token.\n\nReturns:\n-------\n    JSONResponse: A JSON object with the deletion status.\n\nRaises:\n------\n    HTTPException: If the vector store is not found or deletion fails.",
        "operationId": "delete_vector_store_v1_vector_stores__vector_store_id__delete",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "vector_store_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Vector Store Id"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/vector_stores/{vector_store_id}/files": {
      "post": {
        "tags": [
          "Vector Stores"
        ],
        "summary": "Create Vector Store File",
        "description": "Attach a file to an existing vector store and initiate embedding generation.\n\nArgs:\n----\n    vector_store_id (str): The ID of the vector store to attach the file to.\n    file_data (VectorStoreFileCreate): The file data containing the file_id to attach.\n    background_tasks (BackgroundTasks): FastAPI background tasks for asynchronous processing.\n    auth (AuthToken): The authentication token for the current user.\n\nReturns:\n-------\n    VectorStore: The updated vector store object with the newly attached file.\n\nRaises:\n------\n    HTTPException:\n        - 404 if the vector store is not found.\n        - 500 if file attachment fails or if there's an error updating the vector store.\n\nNotes:\n-----\n    - This function updates the vector store by adding the new file_id to its list of files.\n    - It queues a background task to generate embeddings for the newly attached file.\n    - The vector store's status is set to \"in_progress\" as embedding generation begins.",
        "operationId": "create_vector_store_file_v1_vector_stores__vector_store_id__files_post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "vector_store_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Vector Store Id"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/VectorStoreFileCreate"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      },
      "get": {
        "tags": [
          "Vector Stores"
        ],
        "summary": "List Vector Store Files",
        "description": "List all files in a vector store.",
        "operationId": "list_vector_store_files_v1_vector_stores__vector_store_id__files_get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "vector_store_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Vector Store Id"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/vector_stores/{vector_store_id}/files/{file_id}": {
      "delete": {
        "tags": [
          "Vector Stores"
        ],
        "summary": "Remove File From Vector Stores",
        "description": "Remove a file from all vector stores.",
        "operationId": "remove_file_from_vector_stores_v1_vector_stores__vector_store_id__files__file_id__delete",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "file_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "File Id"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/vector_stores/{vector_store_id}/search": {
      "post": {
        "tags": [
          "Vector Stores"
        ],
        "summary": "Query Vector Store",
        "description": "Perform a similarity search on the specified vector store.\n\nArgs:\n----\n    vector_store_id (str): The ID of the vector store to search.\n    request (QueryVectorStoreRequest): The request containing the query text.\n    auth (AuthToken): The authentication token for the request.\n\nReturns:\n-------\n    List[Dict]: A list of search results, each containing the document content and metadata.\n\nRaises:\n------\n    HTTPException: If the vector store is not found or if there's an error during the search.",
        "operationId": "query_vector_store_v1_vector_stores__vector_store_id__search_post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "vector_store_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Vector Store Id"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/QueryVectorStoreRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/vector_stores/{vector_store_id}/list/files/filename/{filename}": {
      "get": {
        "tags": [
          "Vector Stores"
        ],
        "summary": "Get Vector Store File",
        "operationId": "get_vector_store_file_v1_vector_stores__vector_store_id__list_files_filename__filename__get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "vector_store_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Vector Store Id"
            }
          },
          {
            "name": "filename",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Filename"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/vector_stores/from_source": {
      "post": {
        "tags": [
          "Vector Stores"
        ],
        "summary": "Create Vector Store From Source",
        "description": "Create a new vector store from a source (currently only GitHub).\n\nArgs:\n----\n    request (CreateVectorStoreFromSourceRequest): The request containing vector store and source details.\n    background_tasks (BackgroundTasks): FastAPI background tasks.\n    auth (AuthToken): The authentication token.\n\nReturns:\n-------\n    VectorStore: The created vector store object.\n\nRaises:\n------\n    HTTPException: If the vector store creation fails.",
        "operationId": "create_vector_store_from_source_v1_vector_stores_from_source_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateVectorStoreFromSourceRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/VectorStore"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/vector_stores/memory/query": {
      "post": {
        "tags": [
          "Vector Stores"
        ],
        "summary": "Query User Memory",
        "description": "Get relevant memory/context for a user based on a query.\n\nThis endpoint searches a dedicated vector store containing the user's memory/context\nand returns relevant matches based on the query.\n\nArgs:\n----\n    request: The request containing the query text\n    auth: The auth token of the requesting user\n\nReturns:\n-------\n    List of relevant memory entries with their content and metadata",
        "operationId": "query_user_memory_v1_vector_stores_memory_query_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/QueryVectorStoreRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/vector_stores/memory": {
      "post": {
        "tags": [
          "Vector Stores"
        ],
        "summary": "Add User Memory",
        "description": "Add a new memory entry to the user's memory store.",
        "operationId": "add_user_memory_v1_vector_stores_memory_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/AddUserMemoryRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/AddUserMemoryResponse"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/files": {
      "post": {
        "tags": [
          "Files"
        ],
        "summary": "Upload File",
        "description": "Upload a file to the system and create a corresponding database record.\n\nThis function handles file uploads, determines the content type, checks for\nsupported file types and encodings, and stores the file in the configured\nstorage system.\n\nArgs:\n----\n    file (UploadFile): The file to be uploaded.\n    purpose (str): The purpose of the file upload. Must be one of:\n                   \"assistants\", \"batch\", \"fine-tune\", \"vision\".\n    auth (AuthToken): The authentication token for the current user.\n\nReturns:\n-------\n    FileObject: An object containing details of the uploaded file.\n\nRaises:\n------\n    HTTPException:\n        - 400 if the purpose is invalid, file type is not supported,\n          or file encoding is not supported.\n        - 404 if the file details are not found after creation.\n        - 500 if there's an error during file upload or database operations.",
        "operationId": "upload_file_v1_files_post",
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Body_upload_file_v1_files_post"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/FileObject"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/files/{file_id}": {
      "delete": {
        "tags": [
          "Files"
        ],
        "summary": "Delete File",
        "operationId": "delete_file_v1_files__file_id__delete",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "file_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "description": "The ID of the file to delete",
              "title": "File Id"
            },
            "description": "The ID of the file to delete"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      },
      "get": {
        "tags": [
          "Files"
        ],
        "summary": "Retrieve File",
        "description": "Retrieve information about a specific file.\n\nArgs:\n----\n    file_id (str): The ID of the file to retrieve.\n    auth (AuthToken): The authentication token for the current user.\n\nReturns:\n-------\n    FileObject: An object containing details of the requested file.\n\nRaises:\n------\n    HTTPException:\n        - 404 if the file is not found.\n        - 403 if the user doesn't have permission to access the file.",
        "operationId": "retrieve_file_v1_files__file_id__get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "file_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "description": "The ID of the file to retrieve",
              "title": "File Id"
            },
            "description": "The ID of the file to retrieve"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/FileObject"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/files/{file_id}/content": {
      "get": {
        "tags": [
          "Files"
        ],
        "summary": "Retrieve File Content",
        "description": "Retrieve the contents of a specific file.\n\nArgs:\n----\n    file_id (str): The ID of the file to retrieve.\n    auth (AuthToken): The authentication token for the current user.\n\nReturns:\n-------\n    StreamingResponse: A streaming response containing the file content.\n\nRaises:\n------\n    HTTPException:\n        - 404 if the file is not found.\n        - 403 if the user doesn't have permission to access the file.\n        - 500 if there's an error retrieving the file content.",
        "operationId": "retrieve_file_content_v1_files__file_id__content_get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "file_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "description": "The ID of the file to retrieve",
              "title": "File Id"
            },
            "description": "The ID of the file to retrieve"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/threads": {
      "post": {
        "tags": [
          "Threads"
        ],
        "summary": "Create Thread",
        "operationId": "create_thread_v1_threads_post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ThreadCreateParams"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Thread"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      },
      "get": {
        "tags": [
          "Threads"
        ],
        "summary": "List Threads",
        "operationId": "list_threads_v1_threads_get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "include_subthreads",
            "in": "query",
            "required": false,
            "schema": {
              "anyOf": [
                {
                  "type": "boolean"
                },
                {
                  "type": "null"
                }
              ],
              "description": "Include threads that have a parent_id - defaults to true",
              "default": true,
              "title": "Include Subthreads"
            },
            "description": "Include threads that have a parent_id - defaults to true"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Thread"
                  },
                  "title": "Response List Threads V1 Threads Get"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/threads/{thread_id}": {
      "get": {
        "tags": [
          "Threads"
        ],
        "summary": "Get Thread",
        "operationId": "get_thread_v1_threads__thread_id__get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "thread_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Thread Id"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Thread"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "Threads"
        ],
        "summary": "Update Thread",
        "operationId": "update_thread_v1_threads__thread_id__post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "thread_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Thread Id"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ThreadUpdateParams"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Thread"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Threads"
        ],
        "summary": "Delete Thread",
        "operationId": "delete_thread_v1_threads__thread_id__delete",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "thread_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Thread Id"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ThreadDeletionStatus"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/threads/{thread_id}/fork": {
      "post": {
        "tags": [
          "Threads"
        ],
        "summary": "Fork Thread",
        "operationId": "fork_thread_v1_threads__thread_id__fork_post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "thread_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Thread Id"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ThreadForkResponse"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/threads/{parent_id}/subthread": {
      "post": {
        "tags": [
          "Threads"
        ],
        "summary": "Create Subthread",
        "operationId": "create_subthread_v1_threads__parent_id__subthread_post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "parent_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Parent Id"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/SubthreadCreateParams"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Thread"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/threads/{thread_id}/messages": {
      "post": {
        "tags": [
          "Threads"
        ],
        "summary": "Create Message",
        "operationId": "create_message_v1_threads__thread_id__messages_post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "thread_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Thread Id"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MessageCreateParams"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Message-Output"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      },
      "get": {
        "tags": [
          "Threads"
        ],
        "summary": "List Messages",
        "operationId": "list_messages_v1_threads__thread_id__messages_get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "thread_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Thread Id"
            }
          },
          {
            "name": "after",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "description": "A cursor for use in pagination. `after` is an object ID that defines your place in the list.",
              "title": "After"
            },
            "description": "A cursor for use in pagination. `after` is an object ID that defines your place in the list."
          },
          {
            "name": "before",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "description": "A cursor for use in pagination. `before` is an object ID that defines your place in the list.",
              "title": "Before"
            },
            "description": "A cursor for use in pagination. `before` is an object ID that defines your place in the list."
          },
          {
            "name": "limit",
            "in": "query",
            "required": false,
            "schema": {
              "type": "integer",
              "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100.",
              "default": 20,
              "title": "Limit"
            },
            "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100."
          },
          {
            "name": "order",
            "in": "query",
            "required": false,
            "schema": {
              "enum": [
                "asc",
                "desc"
              ],
              "type": "string",
              "description": "Sort order by the `created_at` timestamp of the objects.",
              "default": "desc",
              "title": "Order"
            },
            "description": "Sort order by the `created_at` timestamp of the objects."
          },
          {
            "name": "run_id",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "description": "Filter messages by the run ID that generated them.",
              "title": "Run Id"
            },
            "description": "Filter messages by the run ID that generated them."
          },
          {
            "name": "include_subthreads",
            "in": "query",
            "required": false,
            "schema": {
              "type": "boolean",
              "default": true,
              "title": "Include Subthreads"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListMessagesResponse"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/threads/{thread_id}/messages/{message_id}": {
      "patch": {
        "tags": [
          "Threads"
        ],
        "summary": "Modify Message",
        "operationId": "modify_message_v1_threads__thread_id__messages__message_id__patch",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "message_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Message Id"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MessageUpdateParams"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Message-Output"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/threads/{thread_id}/runs": {
      "post": {
        "tags": [
          "Threads"
        ],
        "summary": "Create Run",
        "operationId": "create_run_v1_threads__thread_id__runs_post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "thread_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Thread Id"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RunCreateParamsBase"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/threads/{thread_id}/stream/{run_id}": {
      "get": {
        "tags": [
          "Threads"
        ],
        "summary": "Thread Subscribe",
        "description": "Subscribe to deltas for a thread and run (for client channels outside of the run).",
        "operationId": "thread_subscribe_v1_threads__thread_id__stream__run_id__get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "thread_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Thread Id"
            }
          },
          {
            "name": "run_id",
            "in": "path",
            "required": true,
            "schema": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ],
              "title": "Run Id"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/threads/{thread_id}/runs/{run_id}": {
      "get": {
        "tags": [
          "Threads"
        ],
        "summary": "Get Run",
        "description": "Get details of a specific run for a thread.",
        "operationId": "get_run_v1_threads__thread_id__runs__run_id__get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "thread_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "description": "The ID of the thread",
              "title": "Thread Id"
            },
            "description": "The ID of the thread"
          },
          {
            "name": "run_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "description": "The ID of the run",
              "title": "Run Id"
            },
            "description": "The ID of the run"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Run"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "Threads"
        ],
        "summary": "Update Run",
        "operationId": "update_run_v1_threads__thread_id__runs__run_id__post",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "thread_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Thread Id"
            }
          },
          {
            "name": "run_id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Run Id"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RunUpdateParams"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Run"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/create_hub_secret": {
      "post": {
        "tags": [
          "Hub Secrets"
        ],
        "summary": "Create Hub Secret",
        "description": "Create a hub secret.",
        "operationId": "create_hub_secret_v1_create_hub_secret_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateHubSecretRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/remove_hub_secret": {
      "post": {
        "tags": [
          "Hub Secrets"
        ],
        "summary": "Remove Hub Secret",
        "description": "Remove a hub secret.",
        "operationId": "remove_hub_secret_v1_remove_hub_secret_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RemoveHubSecretRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/v1/get_user_secrets": {
      "get": {
        "tags": [
          "Hub Secrets"
        ],
        "summary": "Get User Secrets",
        "description": "Get hub secrets for a given user.",
        "operationId": "get_user_secrets_v1_get_user_secrets_get",
        "security": [
          {
            "HTTPBearer": []
          }
        ],
        "parameters": [
          {
            "name": "limit",
            "in": "query",
            "required": false,
            "schema": {
              "anyOf": [
                {
                  "type": "integer"
                },
                {
                  "type": "null"
                }
              ],
              "description": "Limit of the results",
              "default": 100,
              "title": "Limit"
            },
            "description": "Limit of the results"
          },
          {
            "name": "offset",
            "in": "query",
            "required": false,
            "schema": {
              "anyOf": [
                {
                  "type": "integer"
                },
                {
                  "type": "null"
                }
              ],
              "description": "Offset for pagination",
              "default": 0,
              "title": "Offset"
            },
            "description": "Offset for pagination"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/v1/schedule_run": {
      "post": {
        "tags": [
          "Run Schedule"
        ],
        "summary": "Schedule Run",
        "description": "Endpoint to schedule a new run.",
        "operationId": "schedule_run_v1_schedule_run_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateScheduleRunRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          }
        ]
      }
    },
    "/health": {
      "get": {
        "summary": "Health",
        "operationId": "health_health_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "AddUserMemoryRequest": {
        "properties": {
          "memory": {
            "type": "string",
            "title": "Memory"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "memory"
        ],
        "title": "AddUserMemoryRequest"
      },
      "AddUserMemoryResponse": {
        "properties": {
          "status": {
            "type": "string",
            "title": "Status"
          },
          "memory_id": {
            "type": "string",
            "title": "Memory Id"
          },
          "object": {
            "type": "string",
            "title": "Object",
            "default": "memory.created"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "status",
          "memory_id"
        ],
        "title": "AddUserMemoryResponse",
        "description": "Response model for adding user memory."
      },
      "AdditionalMessage": {
        "properties": {
          "content": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "items": {
                  "anyOf": [
                    {
                      "$ref": "#/components/schemas/ImageFileContentBlockParam"
                    },
                    {
                      "$ref": "#/components/schemas/ImageURLContentBlockParam"
                    },
                    {
                      "$ref": "#/components/schemas/TextContentBlockParam"
                    }
                  ]
                },
                "type": "array"
              }
            ],
            "title": "Content"
          },
          "role": {
            "type": "string",
            "enum": [
              "user",
              "assistant"
            ],
            "title": "Role"
          },
          "attachments": {
            "anyOf": [
              {
                "items": {
                  "$ref": "#/components/schemas/AdditionalMessageAttachment"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Attachments"
          },
          "metadata": {
            "anyOf": [
              {
                "additionalProperties": {
                  "type": "string"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metadata"
          }
        },
        "type": "object",
        "required": [
          "content",
          "role"
        ],
        "title": "AdditionalMessage"
      },
      "AdditionalMessageAttachment": {
        "properties": {
          "file_id": {
            "type": "string",
            "title": "File Id"
          },
          "tools": {
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/CodeInterpreterToolParam"
                },
                {
                  "$ref": "#/components/schemas/AdditionalMessageAttachmentToolFileSearch"
                }
              ]
            },
            "type": "array",
            "title": "Tools"
          }
        },
        "type": "object",
        "title": "AdditionalMessageAttachment"
      },
      "AdditionalMessageAttachmentToolFileSearch": {
        "properties": {
          "type": {
            "type": "string",
            "const": "file_search",
            "title": "Type"
          }
        },
        "type": "object",
        "required": [
          "type"
        ],
        "title": "AdditionalMessageAttachmentToolFileSearch"
      },
      "AgentData": {
        "properties": {
          "namespace": {
            "type": "string",
            "title": "Namespace"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "key": {
            "type": "string",
            "title": "Key"
          },
          "value": {
            "type": "object",
            "title": "Value"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "title": "Created At",
            "default": "2025-05-01T18:00:59.636511Z"
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "title": "Updated At"
          }
        },
        "type": "object",
        "required": [
          "namespace",
          "name",
          "key"
        ],
        "title": "AgentData",
        "description": "Agent key value storage."
      },
      "AgentDataRequest": {
        "properties": {
          "key": {
            "type": "string",
            "title": "Key"
          },
          "value": {
            "type": "object",
            "title": "Value"
          }
        },
        "type": "object",
        "required": [
          "key",
          "value"
        ],
        "title": "AgentDataRequest"
      },
      "AssistantToolChoice": {
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "function",
              "code_interpreter",
              "file_search"
            ],
            "title": "Type"
          },
          "function": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/AssistantToolChoiceFunction"
              },
              {
                "type": "null"
              }
            ]
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "type"
        ],
        "title": "AssistantToolChoice"
      },
      "AssistantToolChoiceFunction": {
        "properties": {
          "name": {
            "type": "string",
            "title": "Name"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "name"
        ],
        "title": "AssistantToolChoiceFunction"
      },
      "Attachment": {
        "properties": {
          "file_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "File Id"
          },
          "tools": {
            "anyOf": [
              {
                "items": {
                  "anyOf": [
                    {
                      "$ref": "#/components/schemas/CodeInterpreterTool"
                    },
                    {
                      "$ref": "#/components/schemas/AttachmentToolAssistantToolsFileSearchTypeOnly"
                    }
                  ]
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Tools"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "title": "Attachment"
      },
      "AttachmentToolAssistantToolsFileSearchTypeOnly": {
        "properties": {
          "type": {
            "type": "string",
            "const": "file_search",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "type"
        ],
        "title": "AttachmentToolAssistantToolsFileSearchTypeOnly"
      },
      "AutoFileChunkingStrategyParam": {
        "properties": {
          "type": {
            "type": "string",
            "const": "auto",
            "title": "Type"
          }
        },
        "type": "object",
        "required": [
          "type"
        ],
        "title": "AutoFileChunkingStrategyParam"
      },
      "BenchmarkOutput": {
        "properties": {
          "id": {
            "type": "integer",
            "title": "Id"
          },
          "namespace": {
            "type": "string",
            "title": "Namespace"
          },
          "benchmark": {
            "type": "string",
            "title": "Benchmark"
          },
          "solver": {
            "type": "string",
            "title": "Solver"
          },
          "args": {
            "type": "string",
            "title": "Args"
          },
          "solved": {
            "type": "integer",
            "title": "Solved"
          },
          "total": {
            "type": "integer",
            "title": "Total"
          }
        },
        "type": "object",
        "required": [
          "id",
          "namespace",
          "benchmark",
          "solver",
          "args",
          "solved",
          "total"
        ],
        "title": "BenchmarkOutput"
      },
      "BenchmarkResultOutput": {
        "properties": {
          "index": {
            "type": "integer",
            "title": "Index"
          },
          "solved": {
            "type": "boolean",
            "title": "Solved"
          },
          "info": {
            "type": "string",
            "title": "Info"
          }
        },
        "type": "object",
        "required": [
          "index",
          "solved",
          "info"
        ],
        "title": "BenchmarkResultOutput"
      },
      "Body_add_job_v1_jobs_add_job_post": {
        "properties": {
          "entry_location": {
            "$ref": "#/components/schemas/EntryLocation"
          }
        },
        "type": "object",
        "required": [
          "entry_location"
        ],
        "title": "Body_add_job_v1_jobs_add_job_post"
      },
      "Body_add_star_v1_stars_add_star_post": {
        "properties": {
          "namespace": {
            "type": "string",
            "title": "Namespace"
          },
          "name": {
            "type": "string",
            "title": "Name"
          }
        },
        "type": "object",
        "required": [
          "namespace",
          "name"
        ],
        "title": "Body_add_star_v1_stars_add_star_post"
      },
      "Body_download_file_v1_registry_download_file_post": {
        "properties": {
          "path": {
            "type": "string",
            "title": "Path"
          },
          "entry_location": {
            "$ref": "#/components/schemas/EntryLocation"
          }
        },
        "type": "object",
        "required": [
          "path",
          "entry_location"
        ],
        "title": "Body_download_file_v1_registry_download_file_post"
      },
      "Body_download_metadata_v1_registry_download_metadata_post": {
        "properties": {
          "entry_location": {
            "$ref": "#/components/schemas/EntryLocation"
          }
        },
        "type": "object",
        "required": [
          "entry_location"
        ],
        "title": "Body_download_metadata_v1_registry_download_metadata_post"
      },
      "Body_fork_entry_v1_registry_fork_post": {
        "properties": {
          "modifications": {
            "$ref": "#/components/schemas/ForkEntryModifications"
          },
          "entry_location": {
            "$ref": "#/components/schemas/EntryLocation"
          }
        },
        "type": "object",
        "required": [
          "modifications",
          "entry_location"
        ],
        "title": "Body_fork_entry_v1_registry_fork_post"
      },
      "Body_list_files_v1_registry_list_files_post": {
        "properties": {
          "entry_location": {
            "$ref": "#/components/schemas/EntryLocation"
          }
        },
        "type": "object",
        "required": [
          "entry_location"
        ],
        "title": "Body_list_files_v1_registry_list_files_post"
      },
      "Body_remove_star_v1_stars_remove_star_post": {
        "properties": {
          "namespace": {
            "type": "string",
            "title": "Namespace"
          },
          "name": {
            "type": "string",
            "title": "Name"
          }
        },
        "type": "object",
        "required": [
          "namespace",
          "name"
        ],
        "title": "Body_remove_star_v1_stars_remove_star_post"
      },
      "Body_upload_file_v1_files_post": {
        "properties": {
          "file": {
            "type": "string",
            "format": "binary",
            "title": "File"
          },
          "purpose": {
            "type": "string",
            "enum": [
              "assistants",
              "batch",
              "fine-tune",
              "vision"
            ],
            "title": "Purpose"
          }
        },
        "type": "object",
        "required": [
          "file",
          "purpose"
        ],
        "title": "Body_upload_file_v1_files_post"
      },
      "Body_upload_file_v1_registry_upload_file_post": {
        "properties": {
          "path": {
            "type": "string",
            "title": "Path"
          },
          "file": {
            "type": "string",
            "format": "binary",
            "title": "File"
          },
          "namespace": {
            "type": "string",
            "title": "Namespace"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "version": {
            "type": "string",
            "title": "Version"
          }
        },
        "type": "object",
        "required": [
          "path",
          "file",
          "namespace",
          "name",
          "version"
        ],
        "title": "Body_upload_file_v1_registry_upload_file_post"
      },
      "Body_upload_metadata_v1_registry_upload_metadata_post": {
        "properties": {
          "metadata": {
            "$ref": "#/components/schemas/EntryMetadataInput"
          },
          "entry_location": {
            "$ref": "#/components/schemas/EntryLocation"
          }
        },
        "type": "object",
        "required": [
          "metadata",
          "entry_location"
        ],
        "title": "Body_upload_metadata_v1_registry_upload_metadata_post"
      },
      "ChatCompletionsRequest": {
        "properties": {
          "model": {
            "type": "string",
            "title": "Model",
            "default": "fireworks::accounts/fireworks/models/mixtral-8x22b-instruct"
          },
          "provider": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Provider",
            "default": "fireworks"
          },
          "max_tokens": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Max Tokens",
            "default": 1024
          },
          "logprobs": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Logprobs"
          },
          "temperature": {
            "type": "number",
            "title": "Temperature",
            "default": 1
          },
          "top_p": {
            "type": "number",
            "title": "Top P",
            "default": 1
          },
          "frequency_penalty": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Frequency Penalty",
            "default": 0
          },
          "n": {
            "type": "integer",
            "title": "N",
            "default": 1
          },
          "stop": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Stop"
          },
          "response_format": {
            "anyOf": [
              {
                "type": "string",
                "const": "auto"
              },
              {
                "$ref": "#/components/schemas/openai__types__shared__response_format_text__ResponseFormatText"
              },
              {
                "$ref": "#/components/schemas/openai__types__shared__response_format_json_object__ResponseFormatJSONObject"
              },
              {
                "$ref": "#/components/schemas/openai__types__shared__response_format_json_schema__ResponseFormatJSONSchema-Input"
              },
              {
                "type": "null"
              }
            ],
            "title": "Response Format"
          },
          "stream": {
            "type": "boolean",
            "title": "Stream",
            "default": false
          },
          "tools": {
            "anyOf": [
              {
                "items": {},
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Tools",
            "default": []
          },
          "messages": {
            "items": {
              "$ref": "#/components/schemas/hub__api__v1__completions__Message"
            },
            "type": "array",
            "title": "Messages"
          }
        },
        "type": "object",
        "required": [
          "messages"
        ],
        "title": "ChatCompletionsRequest",
        "description": "Request for chat completions."
      },
      "ChunkingStrategy": {
        "properties": {},
        "type": "object",
        "title": "ChunkingStrategy",
        "description": "Defines the chunking strategy for vector stores."
      },
      "CodeInterpreterTool": {
        "properties": {
          "type": {
            "type": "string",
            "const": "code_interpreter",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "type"
        ],
        "title": "CodeInterpreterTool"
      },
      "CodeInterpreterToolParam": {
        "properties": {
          "type": {
            "type": "string",
            "const": "code_interpreter",
            "title": "Type"
          }
        },
        "type": "object",
        "required": [
          "type"
        ],
        "title": "CodeInterpreterToolParam"
      },
      "CompletionsRequest": {
        "properties": {
          "model": {
            "type": "string",
            "title": "Model",
            "default": "fireworks::accounts/fireworks/models/mixtral-8x22b-instruct"
          },
          "provider": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Provider",
            "default": "fireworks"
          },
          "max_tokens": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Max Tokens",
            "default": 1024
          },
          "logprobs": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Logprobs"
          },
          "temperature": {
            "type": "number",
            "title": "Temperature",
            "default": 1
          },
          "top_p": {
            "type": "number",
            "title": "Top P",
            "default": 1
          },
          "frequency_penalty": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Frequency Penalty",
            "default": 0
          },
          "n": {
            "type": "integer",
            "title": "N",
            "default": 1
          },
          "stop": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Stop"
          },
          "response_format": {
            "anyOf": [
              {
                "type": "string",
                "const": "auto"
              },
              {
                "$ref": "#/components/schemas/openai__types__shared__response_format_text__ResponseFormatText"
              },
              {
                "$ref": "#/components/schemas/openai__types__shared__response_format_json_object__ResponseFormatJSONObject"
              },
              {
                "$ref": "#/components/schemas/openai__types__shared__response_format_json_schema__ResponseFormatJSONSchema-Input"
              },
              {
                "type": "null"
              }
            ],
            "title": "Response Format"
          },
          "stream": {
            "type": "boolean",
            "title": "Stream",
            "default": false
          },
          "tools": {
            "anyOf": [
              {
                "items": {},
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Tools",
            "default": []
          },
          "prompt": {
            "type": "string",
            "title": "Prompt"
          }
        },
        "type": "object",
        "required": [
          "prompt"
        ],
        "title": "CompletionsRequest",
        "description": "Request for completions."
      },
      "CreateHubSecretRequest": {
        "properties": {
          "namespace": {
            "type": "string",
            "title": "Namespace"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "version": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Version"
          },
          "description": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Description"
          },
          "key": {
            "type": "string",
            "title": "Key"
          },
          "value": {
            "type": "string",
            "title": "Value"
          },
          "category": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Category",
            "default": "agent"
          }
        },
        "type": "object",
        "required": [
          "namespace",
          "name",
          "version",
          "description",
          "key",
          "value"
        ],
        "title": "CreateHubSecretRequest",
        "description": "Request model for creating a new hub secret."
      },
      "CreateScheduleRunRequest": {
        "properties": {
          "agent": {
            "type": "string",
            "title": "Agent"
          },
          "input_message": {
            "type": "string",
            "title": "Input Message"
          },
          "run_params": {
            "additionalProperties": {
              "type": "string"
            },
            "type": "object",
            "title": "Run Params"
          },
          "thread_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Thread Id"
          },
          "run_at": {
            "type": "string",
            "format": "date-time",
            "title": "Run At"
          }
        },
        "type": "object",
        "required": [
          "agent",
          "input_message",
          "run_params",
          "thread_id",
          "run_at"
        ],
        "title": "CreateScheduleRunRequest",
        "description": "Request model for creating a new scheduled run."
      },
      "CreateThreadAndRunRequest": {
        "properties": {
          "agent_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Agent Id",
            "description": "The name or identifier of the agent to use to execute this run. Either `agent_id` or `assistant_id` must be provided."
          },
          "assistant_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Assistant Id",
            "description": "An OpenAI compatibility alias for agent. The ID of the [assistant](/docs/api-reference/assistants) to use to execute this run."
          },
          "thread_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Thread Id",
            "description": "The thread to write messages to. If no thread is provided, an empty thread will be created."
          },
          "new_message": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "New Message",
            "description": "A message to add to the thread before running the agents."
          },
          "max_iterations": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Max Iterations",
            "description": "Allow an agent to run for up to this number of iterations.",
            "default": 10
          },
          "record_run": {
            "anyOf": [
              {
                "type": "boolean"
              },
              {
                "type": "null"
              }
            ],
            "title": "Record Run",
            "description": "Whether to record the run in the registry.",
            "default": true
          },
          "tool_resources": {
            "anyOf": [
              {
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Tool Resources",
            "description": "A dictionary of tool resources to use for the run."
          },
          "user_env_vars": {
            "anyOf": [
              {
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "User Env Vars",
            "description": "Env vars provided by the user"
          }
        },
        "type": "object",
        "title": "CreateThreadAndRunRequest"
      },
      "CreateVectorStoreFromSourceRequest": {
        "properties": {
          "name": {
            "type": "string",
            "title": "Name"
          },
          "source": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/GitHubSource"
              },
              {
                "$ref": "#/components/schemas/GitLabSource"
              }
            ],
            "title": "Source"
          },
          "source_auth": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Source Auth"
          },
          "chunking_strategy": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ChunkingStrategy"
              },
              {
                "type": "null"
              }
            ]
          },
          "expires_after": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ExpiresAfter-Input"
              },
              {
                "type": "null"
              }
            ]
          },
          "metadata": {
            "anyOf": [
              {
                "additionalProperties": {
                  "type": "string"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metadata"
          }
        },
        "type": "object",
        "required": [
          "name",
          "source"
        ],
        "title": "CreateVectorStoreFromSourceRequest"
      },
      "CreateVectorStoreRequest": {
        "properties": {
          "chunking_strategy": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/AutoFileChunkingStrategyParam"
              },
              {
                "$ref": "#/components/schemas/StaticFileChunkingStrategyParam"
              },
              {
                "type": "null"
              }
            ],
            "title": "Chunking Strategy"
          },
          "expires_after": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ExpiresAfter-Input"
              },
              {
                "type": "null"
              }
            ]
          },
          "file_ids": {
            "anyOf": [
              {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "File Ids"
          },
          "metadata": {
            "anyOf": [
              {
                "additionalProperties": {
                  "type": "string"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metadata"
          },
          "name": {
            "type": "string",
            "title": "Name"
          }
        },
        "type": "object",
        "required": [
          "name"
        ],
        "title": "CreateVectorStoreRequest",
        "description": "Request model for creating a new vector store."
      },
      "Delegation": {
        "properties": {
          "id": {
            "type": "integer",
            "title": "Id"
          },
          "original_account_id": {
            "type": "string",
            "title": "Original Account Id"
          },
          "delegation_account_id": {
            "type": "string",
            "title": "Delegation Account Id"
          },
          "expires_at": {
            "anyOf": [
              {
                "type": "string",
                "format": "date-time"
              },
              {
                "type": "null"
              }
            ],
            "title": "Expires At"
          }
        },
        "type": "object",
        "required": [
          "original_account_id",
          "delegation_account_id"
        ],
        "title": "Delegation"
      },
      "EmbeddingsRequest": {
        "properties": {
          "input": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              {
                "items": {
                  "type": "integer"
                },
                "type": "array"
              },
              {
                "items": {
                  "items": {
                    "type": "integer"
                  },
                  "type": "array"
                },
                "type": "array"
              }
            ],
            "title": "Input"
          },
          "model": {
            "type": "string",
            "title": "Model",
            "default": "fireworks::nomic-ai/nomic-embed-text-v1.5"
          },
          "provider": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Provider"
          }
        },
        "type": "object",
        "required": [
          "input"
        ],
        "title": "EmbeddingsRequest",
        "description": "Request for embeddings."
      },
      "EntryInformation": {
        "properties": {
          "id": {
            "type": "integer",
            "title": "Id"
          },
          "namespace": {
            "type": "string",
            "title": "Namespace"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "version": {
            "type": "string",
            "title": "Version"
          },
          "updated": {
            "type": "string",
            "format": "date-time",
            "title": "Updated"
          },
          "category": {
            "type": "string",
            "title": "Category"
          },
          "description": {
            "type": "string",
            "title": "Description"
          },
          "details": {
            "type": "object",
            "title": "Details"
          },
          "tags": {
            "items": {
              "type": "string"
            },
            "type": "array",
            "title": "Tags"
          },
          "num_forks": {
            "type": "integer",
            "title": "Num Forks"
          },
          "num_stars": {
            "type": "integer",
            "title": "Num Stars"
          },
          "starred_by_point_of_view": {
            "type": "boolean",
            "title": "Starred By Point Of View"
          },
          "fork_of": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ForkOf"
              },
              {
                "type": "null"
              }
            ]
          }
        },
        "type": "object",
        "required": [
          "id",
          "namespace",
          "name",
          "version",
          "updated",
          "category",
          "description",
          "details",
          "tags",
          "num_forks",
          "num_stars",
          "starred_by_point_of_view",
          "fork_of"
        ],
        "title": "EntryInformation"
      },
      "EntryLocation": {
        "properties": {
          "namespace": {
            "type": "string",
            "title": "Namespace"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "version": {
            "type": "string",
            "title": "Version"
          }
        },
        "type": "object",
        "required": [
          "namespace",
          "name",
          "version"
        ],
        "title": "EntryLocation"
      },
      "EntryMetadata": {
        "properties": {
          "category": {
            "type": "string",
            "title": "Category"
          },
          "description": {
            "type": "string",
            "title": "Description"
          },
          "tags": {
            "items": {
              "type": "string"
            },
            "type": "array",
            "title": "Tags"
          },
          "details": {
            "type": "object",
            "title": "Details"
          },
          "show_entry": {
            "type": "boolean",
            "title": "Show Entry"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "version": {
            "type": "string",
            "title": "Version"
          }
        },
        "type": "object",
        "required": [
          "category",
          "description",
          "tags",
          "details",
          "show_entry",
          "name",
          "version"
        ],
        "title": "EntryMetadata"
      },
      "EntryMetadataInput": {
        "properties": {
          "category": {
            "type": "string",
            "title": "Category"
          },
          "description": {
            "type": "string",
            "title": "Description"
          },
          "tags": {
            "items": {
              "type": "string"
            },
            "type": "array",
            "title": "Tags"
          },
          "details": {
            "type": "object",
            "title": "Details"
          },
          "show_entry": {
            "type": "boolean",
            "title": "Show Entry"
          }
        },
        "type": "object",
        "required": [
          "category",
          "description",
          "tags",
          "details",
          "show_entry"
        ],
        "title": "EntryMetadataInput"
      },
      "EvaluationTable": {
        "properties": {
          "rows": {
            "items": {
              "additionalProperties": {
                "type": "string"
              },
              "type": "object"
            },
            "type": "array",
            "title": "Rows"
          },
          "columns": {
            "items": {
              "type": "string"
            },
            "type": "array",
            "title": "Columns"
          },
          "important_columns": {
            "items": {
              "type": "string"
            },
            "type": "array",
            "title": "Important Columns"
          }
        },
        "type": "object",
        "required": [
          "rows",
          "columns",
          "important_columns"
        ],
        "title": "EvaluationTable"
      },
      "ExpiresAfter-Input": {
        "properties": {
          "anchor": {
            "type": "string",
            "const": "last_active_at",
            "title": "Anchor"
          },
          "days": {
            "type": "integer",
            "title": "Days"
          }
        },
        "type": "object",
        "required": [
          "anchor",
          "days"
        ],
        "title": "ExpiresAfter"
      },
      "ExpiresAfter-Output": {
        "properties": {
          "anchor": {
            "type": "string",
            "const": "last_active_at",
            "title": "Anchor"
          },
          "days": {
            "type": "integer",
            "title": "Days"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "anchor",
          "days"
        ],
        "title": "ExpiresAfter"
      },
      "FileCitation": {
        "properties": {
          "file_id": {
            "type": "string",
            "title": "File Id"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "file_id"
        ],
        "title": "FileCitation"
      },
      "FileCitationAnnotation": {
        "properties": {
          "end_index": {
            "type": "integer",
            "title": "End Index"
          },
          "file_citation": {
            "$ref": "#/components/schemas/FileCitation"
          },
          "start_index": {
            "type": "integer",
            "title": "Start Index"
          },
          "text": {
            "type": "string",
            "title": "Text"
          },
          "type": {
            "type": "string",
            "const": "file_citation",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "end_index",
          "file_citation",
          "start_index",
          "text",
          "type"
        ],
        "title": "FileCitationAnnotation"
      },
      "FileCounts": {
        "properties": {
          "cancelled": {
            "type": "integer",
            "title": "Cancelled"
          },
          "completed": {
            "type": "integer",
            "title": "Completed"
          },
          "failed": {
            "type": "integer",
            "title": "Failed"
          },
          "in_progress": {
            "type": "integer",
            "title": "In Progress"
          },
          "total": {
            "type": "integer",
            "title": "Total"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "cancelled",
          "completed",
          "failed",
          "in_progress",
          "total"
        ],
        "title": "FileCounts"
      },
      "FileObject": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "bytes": {
            "type": "integer",
            "title": "Bytes"
          },
          "created_at": {
            "type": "integer",
            "title": "Created At"
          },
          "filename": {
            "type": "string",
            "title": "Filename"
          },
          "object": {
            "type": "string",
            "const": "file",
            "title": "Object"
          },
          "purpose": {
            "type": "string",
            "enum": [
              "assistants",
              "assistants_output",
              "batch",
              "batch_output",
              "fine-tune",
              "fine-tune-results",
              "vision"
            ],
            "title": "Purpose"
          },
          "status": {
            "type": "string",
            "enum": [
              "uploaded",
              "processed",
              "error"
            ],
            "title": "Status"
          },
          "expires_at": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Expires At"
          },
          "status_details": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Status Details"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "id",
          "bytes",
          "created_at",
          "filename",
          "object",
          "purpose",
          "status"
        ],
        "title": "FileObject"
      },
      "FilePath": {
        "properties": {
          "file_id": {
            "type": "string",
            "title": "File Id"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "file_id"
        ],
        "title": "FilePath"
      },
      "FilePathAnnotation": {
        "properties": {
          "end_index": {
            "type": "integer",
            "title": "End Index"
          },
          "file_path": {
            "$ref": "#/components/schemas/FilePath"
          },
          "start_index": {
            "type": "integer",
            "title": "Start Index"
          },
          "text": {
            "type": "string",
            "title": "Text"
          },
          "type": {
            "type": "string",
            "const": "file_path",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "end_index",
          "file_path",
          "start_index",
          "text",
          "type"
        ],
        "title": "FilePathAnnotation"
      },
      "FileSearch": {
        "properties": {
          "max_num_results": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Max Num Results"
          },
          "ranking_options": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/FileSearchRankingOptions"
              },
              {
                "type": "null"
              }
            ]
          }
        },
        "additionalProperties": true,
        "type": "object",
        "title": "FileSearch"
      },
      "FileSearchRankingOptions": {
        "properties": {
          "score_threshold": {
            "type": "number",
            "title": "Score Threshold"
          },
          "ranker": {
            "anyOf": [
              {
                "type": "string",
                "enum": [
                  "auto",
                  "default_2024_08_21"
                ]
              },
              {
                "type": "null"
              }
            ],
            "title": "Ranker"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "score_threshold"
        ],
        "title": "FileSearchRankingOptions"
      },
      "FileSearchTool": {
        "properties": {
          "type": {
            "type": "string",
            "const": "file_search",
            "title": "Type"
          },
          "file_search": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/FileSearch"
              },
              {
                "type": "null"
              }
            ]
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "type"
        ],
        "title": "FileSearchTool"
      },
      "Filename": {
        "properties": {
          "filename": {
            "type": "string",
            "title": "Filename"
          }
        },
        "type": "object",
        "required": [
          "filename"
        ],
        "title": "Filename"
      },
      "FilterAgentsRequest": {
        "properties": {
          "owner_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Owner Id"
          },
          "with_capabilities": {
            "anyOf": [
              {
                "type": "boolean"
              },
              {
                "type": "null"
              }
            ],
            "title": "With Capabilities",
            "default": false
          },
          "latest_versions_only": {
            "anyOf": [
              {
                "type": "boolean"
              },
              {
                "type": "null"
              }
            ],
            "title": "Latest Versions Only",
            "default": true
          },
          "limit": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Limit",
            "default": 100
          },
          "offset": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Offset",
            "default": 0
          }
        },
        "type": "object",
        "required": [
          "owner_id"
        ],
        "title": "FilterAgentsRequest"
      },
      "ForkEntryModifications": {
        "properties": {
          "name": {
            "type": "string",
            "title": "Name"
          },
          "description": {
            "type": "string",
            "title": "Description"
          },
          "version": {
            "type": "string",
            "title": "Version"
          }
        },
        "type": "object",
        "required": [
          "name",
          "description",
          "version"
        ],
        "title": "ForkEntryModifications"
      },
      "ForkOf": {
        "properties": {
          "namespace": {
            "type": "string",
            "title": "Namespace"
          },
          "name": {
            "type": "string",
            "title": "Name"
          }
        },
        "type": "object",
        "required": [
          "namespace",
          "name"
        ],
        "title": "ForkOf"
      },
      "ForkResult": {
        "properties": {
          "status": {
            "type": "string",
            "title": "Status"
          },
          "entry": {
            "$ref": "#/components/schemas/EntryLocation"
          }
        },
        "type": "object",
        "required": [
          "status",
          "entry"
        ],
        "title": "ForkResult"
      },
      "Function": {
        "properties": {
          "arguments": {
            "type": "string",
            "title": "Arguments"
          },
          "name": {
            "type": "string",
            "title": "Name"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "arguments",
          "name"
        ],
        "title": "Function"
      },
      "FunctionDefinition": {
        "properties": {
          "name": {
            "type": "string",
            "title": "Name"
          },
          "description": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Description"
          },
          "parameters": {
            "anyOf": [
              {
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Parameters"
          },
          "strict": {
            "anyOf": [
              {
                "type": "boolean"
              },
              {
                "type": "null"
              }
            ],
            "title": "Strict"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "name"
        ],
        "title": "FunctionDefinition"
      },
      "FunctionTool": {
        "properties": {
          "function": {
            "$ref": "#/components/schemas/FunctionDefinition"
          },
          "type": {
            "type": "string",
            "const": "function",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "function",
          "type"
        ],
        "title": "FunctionTool"
      },
      "GitHubSource": {
        "properties": {
          "type": {
            "type": "string",
            "title": "Type",
            "default": "github"
          },
          "owner": {
            "type": "string",
            "title": "Owner"
          },
          "repo": {
            "type": "string",
            "title": "Repo"
          },
          "branch": {
            "type": "string",
            "title": "Branch",
            "default": "main"
          }
        },
        "type": "object",
        "required": [
          "owner",
          "repo"
        ],
        "title": "GitHubSource"
      },
      "GitLabSource": {
        "properties": {
          "type": {
            "type": "string",
            "title": "Type",
            "default": "gitlab"
          },
          "owner": {
            "type": "string",
            "title": "Owner"
          },
          "repo": {
            "type": "string",
            "title": "Repo"
          },
          "branch": {
            "type": "string",
            "title": "Branch",
            "default": "main"
          }
        },
        "type": "object",
        "required": [
          "owner",
          "repo"
        ],
        "title": "GitLabSource"
      },
      "HTTPValidationError": {
        "properties": {
          "detail": {
            "items": {
              "$ref": "#/components/schemas/ValidationError"
            },
            "type": "array",
            "title": "Detail"
          }
        },
        "type": "object",
        "title": "HTTPValidationError"
      },
      "ImageFile": {
        "properties": {
          "file_id": {
            "type": "string",
            "title": "File Id"
          },
          "detail": {
            "anyOf": [
              {
                "type": "string",
                "enum": [
                  "auto",
                  "low",
                  "high"
                ]
              },
              {
                "type": "null"
              }
            ],
            "title": "Detail"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "file_id"
        ],
        "title": "ImageFile"
      },
      "ImageFileContentBlock": {
        "properties": {
          "image_file": {
            "$ref": "#/components/schemas/ImageFile"
          },
          "type": {
            "type": "string",
            "const": "image_file",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "image_file",
          "type"
        ],
        "title": "ImageFileContentBlock"
      },
      "ImageFileContentBlockParam": {
        "properties": {
          "image_file": {
            "$ref": "#/components/schemas/ImageFileParam"
          },
          "type": {
            "type": "string",
            "const": "image_file",
            "title": "Type"
          }
        },
        "type": "object",
        "required": [
          "image_file",
          "type"
        ],
        "title": "ImageFileContentBlockParam"
      },
      "ImageFileParam": {
        "properties": {
          "file_id": {
            "type": "string",
            "title": "File Id"
          },
          "detail": {
            "type": "string",
            "enum": [
              "auto",
              "low",
              "high"
            ],
            "title": "Detail"
          }
        },
        "type": "object",
        "required": [
          "file_id"
        ],
        "title": "ImageFileParam"
      },
      "ImageGenerationRequest": {
        "properties": {
          "prompt": {
            "type": "string",
            "title": "Prompt"
          },
          "model": {
            "type": "string",
            "title": "Model",
            "default": "fireworks::accounts/fireworks/models/playground-v2-5-1024px-aesthetic"
          },
          "provider": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Provider"
          },
          "init_image": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Init Image"
          },
          "image_strength": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Image Strength"
          },
          "control_image": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Control Image"
          },
          "control_net_name": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Control Net Name"
          },
          "conditioning_scale": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Conditioning Scale"
          },
          "cfg_scale": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Cfg Scale"
          },
          "sampler": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Sampler"
          },
          "steps": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Steps"
          },
          "seed": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Seed",
            "default": 0
          }
        },
        "type": "object",
        "required": [
          "prompt"
        ],
        "title": "ImageGenerationRequest",
        "description": "Request for image generation."
      },
      "ImageURL": {
        "properties": {
          "url": {
            "type": "string",
            "title": "Url"
          },
          "detail": {
            "anyOf": [
              {
                "type": "string",
                "enum": [
                  "auto",
                  "low",
                  "high"
                ]
              },
              {
                "type": "null"
              }
            ],
            "title": "Detail"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "url"
        ],
        "title": "ImageURL"
      },
      "ImageURLContentBlock": {
        "properties": {
          "image_url": {
            "$ref": "#/components/schemas/ImageURL"
          },
          "type": {
            "type": "string",
            "const": "image_url",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "image_url",
          "type"
        ],
        "title": "ImageURLContentBlock"
      },
      "ImageURLContentBlockParam": {
        "properties": {
          "image_url": {
            "$ref": "#/components/schemas/ImageURLParam"
          },
          "type": {
            "type": "string",
            "const": "image_url",
            "title": "Type"
          }
        },
        "type": "object",
        "required": [
          "image_url",
          "type"
        ],
        "title": "ImageURLContentBlockParam"
      },
      "ImageURLParam": {
        "properties": {
          "url": {
            "type": "string",
            "title": "Url"
          },
          "detail": {
            "type": "string",
            "enum": [
              "auto",
              "low",
              "high"
            ],
            "title": "Detail"
          }
        },
        "type": "object",
        "required": [
          "url"
        ],
        "title": "ImageURLParam"
      },
      "JSONSchema-Output": {
        "properties": {
          "name": {
            "type": "string",
            "title": "Name"
          },
          "description": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Description"
          },
          "schema": {
            "anyOf": [
              {
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Schema"
          },
          "strict": {
            "anyOf": [
              {
                "type": "boolean"
              },
              {
                "type": "null"
              }
            ],
            "title": "Strict"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "name"
        ],
        "title": "JSONSchema"
      },
      "Job": {
        "properties": {
          "id": {
            "type": "integer",
            "title": "Id"
          },
          "registry_path": {
            "type": "string",
            "title": "Registry Path"
          },
          "account_id": {
            "type": "string",
            "title": "Account Id"
          },
          "status": {
            "type": "string",
            "title": "Status"
          },
          "worker_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Worker Id"
          },
          "worker_kind": {
            "type": "string",
            "title": "Worker Kind"
          },
          "info": {
            "type": "object",
            "title": "Info"
          },
          "result": {
            "type": "object",
            "title": "Result"
          }
        },
        "type": "object",
        "required": [
          "registry_path",
          "account_id",
          "status",
          "worker_kind"
        ],
        "title": "Job"
      },
      "JobStatus": {
        "type": "string",
        "enum": [
          "pending",
          "processing",
          "completed"
        ],
        "title": "JobStatus"
      },
      "LastError": {
        "properties": {
          "code": {
            "type": "string",
            "enum": [
              "server_error",
              "rate_limit_exceeded",
              "invalid_prompt"
            ],
            "title": "Code"
          },
          "message": {
            "type": "string",
            "title": "Message"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "code",
          "message"
        ],
        "title": "LastError"
      },
      "ListMessagesResponse": {
        "properties": {
          "object": {
            "type": "string",
            "const": "list",
            "title": "Object"
          },
          "data": {
            "items": {
              "$ref": "#/components/schemas/Message-Output"
            },
            "type": "array",
            "title": "Data"
          },
          "has_more": {
            "type": "boolean",
            "title": "Has More"
          },
          "first_id": {
            "type": "string",
            "title": "First Id"
          },
          "last_id": {
            "type": "string",
            "title": "Last Id"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "object",
          "data",
          "has_more",
          "first_id",
          "last_id"
        ],
        "title": "ListMessagesResponse"
      },
      "Log": {
        "properties": {
          "id": {
            "type": "integer",
            "title": "Id"
          },
          "account_id": {
            "type": "string",
            "title": "Account Id"
          },
          "target": {
            "type": "string",
            "title": "Target"
          },
          "info": {
            "type": "object",
            "title": "Info"
          }
        },
        "type": "object",
        "required": [
          "account_id",
          "target"
        ],
        "title": "Log"
      },
      "Message-Output": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "assistant_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Assistant Id"
          },
          "attachments": {
            "anyOf": [
              {
                "items": {
                  "$ref": "#/components/schemas/Attachment"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Attachments"
          },
          "completed_at": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Completed At"
          },
          "content": {
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/ImageFileContentBlock"
                },
                {
                  "$ref": "#/components/schemas/ImageURLContentBlock"
                },
                {
                  "$ref": "#/components/schemas/TextContentBlock"
                },
                {
                  "$ref": "#/components/schemas/RefusalContentBlock"
                }
              ]
            },
            "type": "array",
            "title": "Content"
          },
          "created_at": {
            "type": "integer",
            "title": "Created At"
          },
          "incomplete_at": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Incomplete At"
          },
          "incomplete_details": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/openai__types__beta__threads__message__IncompleteDetails"
              },
              {
                "type": "null"
              }
            ]
          },
          "metadata": {
            "anyOf": [
              {
                "additionalProperties": {
                  "type": "string"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metadata"
          },
          "object": {
            "type": "string",
            "const": "thread.message",
            "title": "Object"
          },
          "role": {
            "type": "string",
            "enum": [
              "user",
              "assistant"
            ],
            "title": "Role"
          },
          "run_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Run Id"
          },
          "status": {
            "type": "string",
            "enum": [
              "in_progress",
              "incomplete",
              "completed"
            ],
            "title": "Status"
          },
          "thread_id": {
            "type": "string",
            "title": "Thread Id"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "id",
          "content",
          "created_at",
          "object",
          "role",
          "status",
          "thread_id"
        ],
        "title": "Message"
      },
      "MessageAttachment": {
        "properties": {
          "file_id": {
            "type": "string",
            "title": "File Id"
          },
          "tools": {
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/CodeInterpreterToolParam"
                },
                {
                  "$ref": "#/components/schemas/MessageAttachmentToolFileSearch"
                }
              ]
            },
            "type": "array",
            "title": "Tools"
          }
        },
        "type": "object",
        "title": "MessageAttachment"
      },
      "MessageAttachmentToolFileSearch": {
        "properties": {
          "type": {
            "type": "string",
            "const": "file_search",
            "title": "Type"
          }
        },
        "type": "object",
        "required": [
          "type"
        ],
        "title": "MessageAttachmentToolFileSearch"
      },
      "MessageCreateParams": {
        "properties": {
          "content": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "items": {
                  "anyOf": [
                    {
                      "$ref": "#/components/schemas/ImageFileContentBlockParam"
                    },
                    {
                      "$ref": "#/components/schemas/ImageURLContentBlockParam"
                    },
                    {
                      "$ref": "#/components/schemas/TextContentBlockParam"
                    }
                  ]
                },
                "type": "array"
              }
            ],
            "title": "Content"
          },
          "role": {
            "type": "string",
            "enum": [
              "user",
              "assistant",
              "system"
            ],
            "title": "Role"
          },
          "attachments": {
            "anyOf": [
              {
                "items": {
                  "$ref": "#/components/schemas/Attachment"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Attachments"
          },
          "metadata": {
            "anyOf": [
              {
                "additionalProperties": {
                  "type": "string"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metadata"
          },
          "assistant_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Assistant Id"
          },
          "run_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Run Id"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "content",
          "role"
        ],
        "title": "MessageCreateParams"
      },
      "MessageUpdateParams": {
        "properties": {
          "thread_id": {
            "type": "string",
            "title": "Thread Id"
          },
          "metadata": {
            "anyOf": [
              {
                "additionalProperties": {
                  "type": "string"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metadata"
          }
        },
        "type": "object",
        "required": [
          "thread_id"
        ],
        "title": "MessageUpdateParams"
      },
      "QueryVectorStoreRequest": {
        "properties": {
          "query": {
            "type": "string",
            "title": "Query"
          },
          "full_files": {
            "type": "boolean",
            "title": "Full Files",
            "default": false
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "query"
        ],
        "title": "QueryVectorStoreRequest",
        "description": "Request model for querying a vector store."
      },
      "RefusalContentBlock": {
        "properties": {
          "refusal": {
            "type": "string",
            "title": "Refusal"
          },
          "type": {
            "type": "string",
            "const": "refusal",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "refusal",
          "type"
        ],
        "title": "RefusalContentBlock"
      },
      "RegistryEntry": {
        "properties": {
          "id": {
            "type": "integer",
            "title": "Id"
          },
          "namespace": {
            "type": "string",
            "title": "Namespace"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "version": {
            "type": "string",
            "title": "Version"
          },
          "time": {
            "type": "string",
            "format": "date-time",
            "title": "Time"
          },
          "description": {
            "type": "string",
            "title": "Description",
            "default": ""
          },
          "category": {
            "type": "string",
            "title": "Category",
            "default": ""
          },
          "details": {
            "type": "object",
            "title": "Details"
          },
          "show_entry": {
            "type": "boolean",
            "title": "Show Entry",
            "default": true
          }
        },
        "type": "object",
        "required": [
          "namespace",
          "name",
          "version"
        ],
        "title": "RegistryEntry",
        "description": "Entry stored in the registry."
      },
      "RemoveHubSecretRequest": {
        "properties": {
          "namespace": {
            "type": "string",
            "title": "Namespace"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "version": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Version"
          },
          "key": {
            "type": "string",
            "title": "Key"
          },
          "category": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Category",
            "default": "agent"
          }
        },
        "type": "object",
        "required": [
          "namespace",
          "name",
          "version",
          "key"
        ],
        "title": "RemoveHubSecretRequest"
      },
      "RequiredAction": {
        "properties": {
          "submit_tool_outputs": {
            "$ref": "#/components/schemas/RequiredActionSubmitToolOutputs"
          },
          "type": {
            "type": "string",
            "const": "submit_tool_outputs",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "submit_tool_outputs",
          "type"
        ],
        "title": "RequiredAction"
      },
      "RequiredActionFunctionToolCall": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "function": {
            "$ref": "#/components/schemas/Function"
          },
          "type": {
            "type": "string",
            "const": "function",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "id",
          "function",
          "type"
        ],
        "title": "RequiredActionFunctionToolCall"
      },
      "RequiredActionSubmitToolOutputs": {
        "properties": {
          "tool_calls": {
            "items": {
              "$ref": "#/components/schemas/RequiredActionFunctionToolCall"
            },
            "type": "array",
            "title": "Tool Calls"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "tool_calls"
        ],
        "title": "RequiredActionSubmitToolOutputs"
      },
      "ResponseFormatJSONObject-Output": {
        "properties": {
          "type": {
            "type": "string",
            "const": "json_object",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "type"
        ],
        "title": "ResponseFormatJSONObject"
      },
      "ResponseFormatJSONSchema-Output": {
        "properties": {
          "json_schema": {
            "$ref": "#/components/schemas/JSONSchema-Output"
          },
          "type": {
            "type": "string",
            "const": "json_schema",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "json_schema",
          "type"
        ],
        "title": "ResponseFormatJSONSchema"
      },
      "ResponseFormatText-Output": {
        "properties": {
          "type": {
            "type": "string",
            "const": "text",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "type"
        ],
        "title": "ResponseFormatText"
      },
      "RevokeNonce": {
        "properties": {
          "nonce": {
            "type": "string",
            "format": "binary",
            "title": "Nonce"
          }
        },
        "type": "object",
        "required": [
          "nonce"
        ],
        "title": "RevokeNonce"
      },
      "Run": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "assistant_id": {
            "type": "string",
            "title": "Assistant Id"
          },
          "cancelled_at": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Cancelled At"
          },
          "completed_at": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Completed At"
          },
          "created_at": {
            "type": "integer",
            "title": "Created At"
          },
          "expires_at": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Expires At"
          },
          "failed_at": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Failed At"
          },
          "incomplete_details": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/openai__types__beta__threads__run__IncompleteDetails"
              },
              {
                "type": "null"
              }
            ]
          },
          "instructions": {
            "type": "string",
            "title": "Instructions"
          },
          "last_error": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/LastError"
              },
              {
                "type": "null"
              }
            ]
          },
          "max_completion_tokens": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Max Completion Tokens"
          },
          "max_prompt_tokens": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Max Prompt Tokens"
          },
          "metadata": {
            "anyOf": [
              {
                "additionalProperties": {
                  "type": "string"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metadata"
          },
          "model": {
            "type": "string",
            "title": "Model"
          },
          "object": {
            "type": "string",
            "const": "thread.run",
            "title": "Object"
          },
          "parallel_tool_calls": {
            "type": "boolean",
            "title": "Parallel Tool Calls"
          },
          "required_action": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/RequiredAction"
              },
              {
                "type": "null"
              }
            ]
          },
          "response_format": {
            "anyOf": [
              {
                "type": "string",
                "const": "auto"
              },
              {
                "$ref": "#/components/schemas/ResponseFormatText-Output"
              },
              {
                "$ref": "#/components/schemas/ResponseFormatJSONObject-Output"
              },
              {
                "$ref": "#/components/schemas/ResponseFormatJSONSchema-Output"
              },
              {
                "type": "null"
              }
            ],
            "title": "Response Format"
          },
          "started_at": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Started At"
          },
          "status": {
            "type": "string",
            "enum": [
              "queued",
              "in_progress",
              "requires_action",
              "cancelling",
              "cancelled",
              "failed",
              "completed",
              "incomplete",
              "expired"
            ],
            "title": "Status"
          },
          "thread_id": {
            "type": "string",
            "title": "Thread Id"
          },
          "tool_choice": {
            "anyOf": [
              {
                "type": "string",
                "enum": [
                  "none",
                  "auto",
                  "required"
                ]
              },
              {
                "$ref": "#/components/schemas/AssistantToolChoice"
              },
              {
                "type": "null"
              }
            ],
            "title": "Tool Choice"
          },
          "tools": {
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/CodeInterpreterTool"
                },
                {
                  "$ref": "#/components/schemas/FileSearchTool"
                },
                {
                  "$ref": "#/components/schemas/FunctionTool"
                }
              ]
            },
            "type": "array",
            "title": "Tools"
          },
          "truncation_strategy": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/TruncationStrategy-Output"
              },
              {
                "type": "null"
              }
            ]
          },
          "usage": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/Usage"
              },
              {
                "type": "null"
              }
            ]
          },
          "temperature": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Temperature"
          },
          "top_p": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Top P"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "id",
          "assistant_id",
          "created_at",
          "instructions",
          "model",
          "object",
          "parallel_tool_calls",
          "status",
          "thread_id",
          "tools"
        ],
        "title": "Run"
      },
      "RunCreateParamsBase": {
        "properties": {
          "assistant_id": {
            "type": "string",
            "title": "Assistant Id",
            "description": "The ID of the assistant to use to execute this run."
          },
          "model": {
            "type": "string",
            "title": "Model",
            "description": "The ID of the Model to be used to execute this run.",
            "default": ""
          },
          "instructions": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Instructions",
            "description": "Overrides the instructions of the assistant. This is useful for modifying the behavior on a per-run basis."
          },
          "tools": {
            "anyOf": [
              {
                "items": {
                  "type": "object"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Tools",
            "description": "Override the tools the assistant can use for this run."
          },
          "metadata": {
            "anyOf": [
              {
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metadata",
            "description": "Set of 16 key-value pairs that can be attached to an object."
          },
          "include": {
            "items": {
              "type": "object"
            },
            "type": "array",
            "title": "Include",
            "description": "A list of additional fields to include in the response.",
            "default": []
          },
          "additional_instructions": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Additional Instructions",
            "description": "Appends additional instructions at the end of the instructions for the run."
          },
          "additional_messages": {
            "anyOf": [
              {
                "items": {
                  "$ref": "#/components/schemas/AdditionalMessage"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Additional Messages",
            "description": "Adds additional messages to the thread before creating the run."
          },
          "max_completion_tokens": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Max Completion Tokens",
            "description": "The maximum number of completion tokens that may be used over the course of the run."
          },
          "max_prompt_tokens": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Max Prompt Tokens",
            "description": "The maximum number of prompt tokens that may be used over the course of the run."
          },
          "parallel_tool_calls": {
            "anyOf": [
              {
                "type": "boolean"
              },
              {
                "type": "null"
              }
            ],
            "title": "Parallel Tool Calls",
            "description": "Whether to enable parallel function calling during tool use."
          },
          "response_format": {
            "anyOf": [
              {
                "type": "string",
                "const": "auto"
              },
              {
                "$ref": "#/components/schemas/openai__types__shared_params__response_format_text__ResponseFormatText"
              },
              {
                "$ref": "#/components/schemas/openai__types__shared_params__response_format_json_object__ResponseFormatJSONObject"
              },
              {
                "$ref": "#/components/schemas/openai__types__shared_params__response_format_json_schema__ResponseFormatJSONSchema"
              },
              {
                "type": "null"
              }
            ],
            "title": "Response Format",
            "description": "Specifies the format that the model must output."
          },
          "temperature": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Temperature",
            "description": "What sampling temperature to use, between 0 and 2."
          },
          "tool_choice": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Tool Choice",
            "description": "Controls which (if any) tool is called by the model."
          },
          "top_p": {
            "anyOf": [
              {
                "type": "number"
              },
              {
                "type": "null"
              }
            ],
            "title": "Top P",
            "description": "An alternative to sampling with temperature, called nucleus sampling."
          },
          "truncation_strategy": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/TruncationStrategy-Input"
              },
              {
                "type": "null"
              }
            ],
            "description": "Controls for how a thread will be truncated prior to the run."
          },
          "stream": {
            "type": "boolean",
            "title": "Stream",
            "description": "Whether to stream the run.",
            "default": false
          },
          "schedule_at": {
            "anyOf": [
              {
                "type": "string",
                "format": "date-time"
              },
              {
                "type": "null"
              }
            ],
            "title": "Schedule At",
            "description": "The time at which the run should be scheduled."
          },
          "delegate_execution": {
            "type": "boolean",
            "title": "Delegate Execution",
            "description": "Whether to delegate execution to an external actor.",
            "default": false
          },
          "parent_run_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Parent Run Id",
            "description": "The ID of the run that this run is triggered by."
          },
          "run_mode": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/RunMode"
              },
              {
                "type": "null"
              }
            ],
            "description": "The mode in which the run should be executed.",
            "default": 0
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "assistant_id"
        ],
        "title": "RunCreateParamsBase"
      },
      "RunMode": {
        "type": "integer",
        "enum": [
          0,
          1
        ],
        "title": "RunMode"
      },
      "RunUpdateParams": {
        "properties": {
          "status": {
            "anyOf": [
              {
                "type": "string",
                "enum": [
                  "requires_action",
                  "failed",
                  "expired",
                  "completed"
                ]
              },
              {
                "type": "null"
              }
            ],
            "title": "Status"
          },
          "completed_at": {
            "anyOf": [
              {
                "type": "string",
                "format": "date-time"
              },
              {
                "type": "null"
              }
            ],
            "title": "Completed At"
          },
          "failed_at": {
            "anyOf": [
              {
                "type": "string",
                "format": "date-time"
              },
              {
                "type": "null"
              }
            ],
            "title": "Failed At"
          },
          "metadata": {
            "anyOf": [
              {
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metadata"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "title": "RunUpdateParams"
      },
      "SelectedJob": {
        "properties": {
          "selected": {
            "type": "boolean",
            "title": "Selected"
          },
          "job": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/Job"
              },
              {
                "type": "null"
              }
            ]
          },
          "registry_path": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Registry Path"
          },
          "info": {
            "type": "string",
            "title": "Info"
          }
        },
        "type": "object",
        "required": [
          "selected",
          "job",
          "registry_path",
          "info"
        ],
        "title": "SelectedJob"
      },
      "StaticFileChunkingStrategyParam": {
        "properties": {
          "chunk_overlap_tokens": {
            "type": "integer",
            "title": "Chunk Overlap Tokens"
          },
          "max_chunk_size_tokens": {
            "type": "integer",
            "title": "Max Chunk Size Tokens"
          }
        },
        "type": "object",
        "required": [
          "chunk_overlap_tokens",
          "max_chunk_size_tokens"
        ],
        "title": "StaticFileChunkingStrategyParam"
      },
      "SubthreadCreateParams": {
        "properties": {
          "messages_to_copy": {
            "anyOf": [
              {
                "items": {
                  "type": "integer"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Messages To Copy",
            "default": []
          },
          "new_messages": {
            "anyOf": [
              {
                "items": {
                  "$ref": "#/components/schemas/MessageCreateParams"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "New Messages",
            "default": []
          }
        },
        "additionalProperties": true,
        "type": "object",
        "title": "SubthreadCreateParams"
      },
      "Text": {
        "properties": {
          "annotations": {
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/FileCitationAnnotation"
                },
                {
                  "$ref": "#/components/schemas/FilePathAnnotation"
                }
              ]
            },
            "type": "array",
            "title": "Annotations"
          },
          "value": {
            "type": "string",
            "title": "Value"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "annotations",
          "value"
        ],
        "title": "Text"
      },
      "TextContentBlock": {
        "properties": {
          "text": {
            "$ref": "#/components/schemas/Text"
          },
          "type": {
            "type": "string",
            "const": "text",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "text",
          "type"
        ],
        "title": "TextContentBlock"
      },
      "TextContentBlockParam": {
        "properties": {
          "text": {
            "type": "string",
            "title": "Text"
          },
          "type": {
            "type": "string",
            "const": "text",
            "title": "Type"
          }
        },
        "type": "object",
        "required": [
          "text",
          "type"
        ],
        "title": "TextContentBlockParam"
      },
      "Thread": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "created_at": {
            "type": "integer",
            "title": "Created At"
          },
          "metadata": {
            "anyOf": [
              {
                "additionalProperties": {
                  "type": "string"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metadata"
          },
          "object": {
            "type": "string",
            "const": "thread",
            "title": "Object"
          },
          "tool_resources": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ToolResources-Output"
              },
              {
                "type": "null"
              }
            ]
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "id",
          "created_at",
          "object"
        ],
        "title": "Thread"
      },
      "ThreadCreateParams": {
        "properties": {
          "messages": {
            "items": {
              "$ref": "#/components/schemas/openai__types__beta__thread_create_params__Message"
            },
            "type": "array",
            "title": "Messages"
          },
          "metadata": {
            "anyOf": [
              {
                "additionalProperties": {
                  "type": "string"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metadata"
          },
          "tool_resources": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ToolResources-Input"
              },
              {
                "type": "null"
              }
            ]
          }
        },
        "type": "object",
        "title": "ThreadCreateParams"
      },
      "ThreadDeletionStatus": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "object": {
            "type": "string",
            "title": "Object",
            "default": "thread.deleted"
          },
          "deleted": {
            "type": "boolean",
            "title": "Deleted",
            "default": true
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "id"
        ],
        "title": "ThreadDeletionStatus"
      },
      "ThreadForkResponse": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "object": {
            "type": "string",
            "title": "Object",
            "default": "thread"
          },
          "created_at": {
            "type": "integer",
            "title": "Created At"
          },
          "metadata": {
            "anyOf": [
              {
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metadata"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "id",
          "created_at"
        ],
        "title": "ThreadForkResponse"
      },
      "ThreadUpdateParams": {
        "properties": {
          "metadata": {
            "anyOf": [
              {
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metadata",
            "description": "Set of 16 key-value pairs that can be attached to an object."
          },
          "tool_resources": {
            "anyOf": [
              {
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Tool Resources",
            "description": "A set of resources that are made available to the assistant's tools in this thread."
          }
        },
        "additionalProperties": true,
        "type": "object",
        "title": "ThreadUpdateParams"
      },
      "ToolResources-Input": {
        "properties": {
          "code_interpreter": {
            "$ref": "#/components/schemas/ToolResourcesCodeInterpreter-Input"
          },
          "file_search": {
            "$ref": "#/components/schemas/ToolResourcesFileSearch-Input"
          }
        },
        "type": "object",
        "title": "ToolResources"
      },
      "ToolResources-Output": {
        "properties": {
          "code_interpreter": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ToolResourcesCodeInterpreter-Output"
              },
              {
                "type": "null"
              }
            ]
          },
          "file_search": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ToolResourcesFileSearch-Output"
              },
              {
                "type": "null"
              }
            ]
          }
        },
        "additionalProperties": true,
        "type": "object",
        "title": "ToolResources"
      },
      "ToolResourcesCodeInterpreter-Input": {
        "properties": {
          "file_ids": {
            "items": {
              "type": "string"
            },
            "type": "array",
            "title": "File Ids"
          }
        },
        "type": "object",
        "title": "ToolResourcesCodeInterpreter"
      },
      "ToolResourcesCodeInterpreter-Output": {
        "properties": {
          "file_ids": {
            "anyOf": [
              {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "File Ids"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "title": "ToolResourcesCodeInterpreter"
      },
      "ToolResourcesFileSearch-Input": {
        "properties": {
          "vector_store_ids": {
            "items": {
              "type": "string"
            },
            "type": "array",
            "title": "Vector Store Ids"
          },
          "vector_stores": {
            "items": {
              "$ref": "#/components/schemas/ToolResourcesFileSearchVectorStore"
            },
            "type": "array",
            "title": "Vector Stores"
          }
        },
        "type": "object",
        "title": "ToolResourcesFileSearch"
      },
      "ToolResourcesFileSearch-Output": {
        "properties": {
          "vector_store_ids": {
            "anyOf": [
              {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Vector Store Ids"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "title": "ToolResourcesFileSearch"
      },
      "ToolResourcesFileSearchVectorStore": {
        "properties": {
          "chunking_strategy": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ToolResourcesFileSearchVectorStoreChunkingStrategyAuto"
              },
              {
                "$ref": "#/components/schemas/ToolResourcesFileSearchVectorStoreChunkingStrategyStatic"
              }
            ],
            "title": "Chunking Strategy"
          },
          "file_ids": {
            "items": {
              "type": "string"
            },
            "type": "array",
            "title": "File Ids"
          },
          "metadata": {
            "anyOf": [
              {
                "additionalProperties": {
                  "type": "string"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metadata"
          }
        },
        "type": "object",
        "title": "ToolResourcesFileSearchVectorStore"
      },
      "ToolResourcesFileSearchVectorStoreChunkingStrategyAuto": {
        "properties": {
          "type": {
            "type": "string",
            "const": "auto",
            "title": "Type"
          }
        },
        "type": "object",
        "required": [
          "type"
        ],
        "title": "ToolResourcesFileSearchVectorStoreChunkingStrategyAuto"
      },
      "ToolResourcesFileSearchVectorStoreChunkingStrategyStatic": {
        "properties": {
          "static": {
            "$ref": "#/components/schemas/ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic"
          },
          "type": {
            "type": "string",
            "const": "static",
            "title": "Type"
          }
        },
        "type": "object",
        "required": [
          "static",
          "type"
        ],
        "title": "ToolResourcesFileSearchVectorStoreChunkingStrategyStatic"
      },
      "ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic": {
        "properties": {
          "chunk_overlap_tokens": {
            "type": "integer",
            "title": "Chunk Overlap Tokens"
          },
          "max_chunk_size_tokens": {
            "type": "integer",
            "title": "Max Chunk Size Tokens"
          }
        },
        "type": "object",
        "required": [
          "chunk_overlap_tokens",
          "max_chunk_size_tokens"
        ],
        "title": "ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic"
      },
      "TruncationStrategy-Input": {
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "auto",
              "last_messages"
            ],
            "title": "Type"
          },
          "last_messages": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Last Messages"
          }
        },
        "type": "object",
        "required": [
          "type"
        ],
        "title": "TruncationStrategy"
      },
      "TruncationStrategy-Output": {
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "auto",
              "last_messages"
            ],
            "title": "Type"
          },
          "last_messages": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Last Messages"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "type"
        ],
        "title": "TruncationStrategy"
      },
      "Usage": {
        "properties": {
          "completion_tokens": {
            "type": "integer",
            "title": "Completion Tokens"
          },
          "prompt_tokens": {
            "type": "integer",
            "title": "Prompt Tokens"
          },
          "total_tokens": {
            "type": "integer",
            "title": "Total Tokens"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "completion_tokens",
          "prompt_tokens",
          "total_tokens"
        ],
        "title": "Usage"
      },
      "ValidationError": {
        "properties": {
          "loc": {
            "items": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "integer"
                }
              ]
            },
            "type": "array",
            "title": "Location"
          },
          "msg": {
            "type": "string",
            "title": "Message"
          },
          "type": {
            "type": "string",
            "title": "Error Type"
          }
        },
        "type": "object",
        "required": [
          "loc",
          "msg",
          "type"
        ],
        "title": "ValidationError"
      },
      "VectorStore": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "created_at": {
            "type": "integer",
            "title": "Created At"
          },
          "file_counts": {
            "$ref": "#/components/schemas/FileCounts"
          },
          "last_active_at": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Last Active At"
          },
          "metadata": {
            "anyOf": [
              {
                "additionalProperties": {
                  "type": "string"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metadata"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "object": {
            "type": "string",
            "const": "vector_store",
            "title": "Object"
          },
          "status": {
            "type": "string",
            "enum": [
              "expired",
              "in_progress",
              "completed"
            ],
            "title": "Status"
          },
          "usage_bytes": {
            "type": "integer",
            "title": "Usage Bytes"
          },
          "expires_after": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ExpiresAfter-Output"
              },
              {
                "type": "null"
              }
            ]
          },
          "expires_at": {
            "anyOf": [
              {
                "type": "integer"
              },
              {
                "type": "null"
              }
            ],
            "title": "Expires At"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "id",
          "created_at",
          "file_counts",
          "name",
          "object",
          "status",
          "usage_bytes"
        ],
        "title": "VectorStore"
      },
      "VectorStoreFileCreate": {
        "properties": {
          "file_id": {
            "type": "string",
            "title": "File Id"
          }
        },
        "type": "object",
        "required": [
          "file_id"
        ],
        "title": "VectorStoreFileCreate",
        "description": "Request model for creating a vector store file."
      },
      "WorkerKind": {
        "type": "string",
        "enum": [
          "GPU_8_A100",
          "CPU_MEDIUM"
        ],
        "title": "WorkerKind"
      },
      "hub__api__v1__completions__Message": {
        "properties": {
          "role": {
            "type": "string",
            "title": "Role"
          },
          "content": {
            "anyOf": [
              {
                "items": {},
                "type": "array"
              },
              {
                "type": "string"
              }
            ],
            "title": "Content"
          }
        },
        "type": "object",
        "required": [
          "role",
          "content"
        ],
        "title": "Message",
        "description": "A chat message."
      },
      "openai__types__beta__thread_create_params__Message": {
        "properties": {
          "content": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "items": {
                  "anyOf": [
                    {
                      "$ref": "#/components/schemas/ImageFileContentBlockParam"
                    },
                    {
                      "$ref": "#/components/schemas/ImageURLContentBlockParam"
                    },
                    {
                      "$ref": "#/components/schemas/TextContentBlockParam"
                    }
                  ]
                },
                "type": "array"
              }
            ],
            "title": "Content"
          },
          "role": {
            "type": "string",
            "enum": [
              "user",
              "assistant"
            ],
            "title": "Role"
          },
          "attachments": {
            "anyOf": [
              {
                "items": {
                  "$ref": "#/components/schemas/MessageAttachment"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Attachments"
          },
          "metadata": {
            "anyOf": [
              {
                "additionalProperties": {
                  "type": "string"
                },
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Metadata"
          }
        },
        "type": "object",
        "required": [
          "content",
          "role"
        ],
        "title": "Message"
      },
      "openai__types__beta__threads__message__IncompleteDetails": {
        "properties": {
          "reason": {
            "type": "string",
            "enum": [
              "content_filter",
              "max_tokens",
              "run_cancelled",
              "run_expired",
              "run_failed"
            ],
            "title": "Reason"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "reason"
        ],
        "title": "IncompleteDetails"
      },
      "openai__types__beta__threads__run__IncompleteDetails": {
        "properties": {
          "reason": {
            "anyOf": [
              {
                "type": "string",
                "enum": [
                  "max_completion_tokens",
                  "max_prompt_tokens"
                ]
              },
              {
                "type": "null"
              }
            ],
            "title": "Reason"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "title": "IncompleteDetails"
      },
      "openai__types__shared__response_format_json_object__ResponseFormatJSONObject": {
        "properties": {
          "type": {
            "type": "string",
            "const": "json_object",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "type"
        ],
        "title": "ResponseFormatJSONObject"
      },
      "openai__types__shared__response_format_json_schema__JSONSchema": {
        "properties": {
          "name": {
            "type": "string",
            "title": "Name"
          },
          "description": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Description"
          },
          "schema": {
            "anyOf": [
              {
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Schema"
          },
          "strict": {
            "anyOf": [
              {
                "type": "boolean"
              },
              {
                "type": "null"
              }
            ],
            "title": "Strict"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "name"
        ],
        "title": "JSONSchema"
      },
      "openai__types__shared__response_format_json_schema__ResponseFormatJSONSchema-Input": {
        "properties": {
          "json_schema": {
            "$ref": "#/components/schemas/openai__types__shared__response_format_json_schema__JSONSchema"
          },
          "type": {
            "type": "string",
            "const": "json_schema",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "json_schema",
          "type"
        ],
        "title": "ResponseFormatJSONSchema"
      },
      "openai__types__shared__response_format_text__ResponseFormatText": {
        "properties": {
          "type": {
            "type": "string",
            "const": "text",
            "title": "Type"
          }
        },
        "additionalProperties": true,
        "type": "object",
        "required": [
          "type"
        ],
        "title": "ResponseFormatText"
      },
      "openai__types__shared_params__response_format_json_object__ResponseFormatJSONObject": {
        "properties": {
          "type": {
            "type": "string",
            "const": "json_object",
            "title": "Type"
          }
        },
        "type": "object",
        "required": [
          "type"
        ],
        "title": "ResponseFormatJSONObject"
      },
      "openai__types__shared_params__response_format_json_schema__JSONSchema": {
        "properties": {
          "name": {
            "type": "string",
            "title": "Name"
          },
          "description": {
            "type": "string",
            "title": "Description"
          },
          "schema": {
            "type": "object",
            "title": "Schema"
          },
          "strict": {
            "anyOf": [
              {
                "type": "boolean"
              },
              {
                "type": "null"
              }
            ],
            "title": "Strict"
          }
        },
        "type": "object",
        "required": [
          "name"
        ],
        "title": "JSONSchema"
      },
      "openai__types__shared_params__response_format_json_schema__ResponseFormatJSONSchema": {
        "properties": {
          "json_schema": {
            "$ref": "#/components/schemas/openai__types__shared_params__response_format_json_schema__JSONSchema"
          },
          "type": {
            "type": "string",
            "const": "json_schema",
            "title": "Type"
          }
        },
        "type": "object",
        "required": [
          "json_schema",
          "type"
        ],
        "title": "ResponseFormatJSONSchema"
      },
      "openai__types__shared_params__response_format_text__ResponseFormatText": {
        "properties": {
          "type": {
            "type": "string",
            "const": "text",
            "title": "Type"
          }
        },
        "type": "object",
        "required": [
          "type"
        ],
        "title": "ResponseFormatText"
      }
    },
    "securitySchemes": {
      "HTTPBearer": {
        "type": "http",
        "scheme": "bearer"
      }
    }
  }
}