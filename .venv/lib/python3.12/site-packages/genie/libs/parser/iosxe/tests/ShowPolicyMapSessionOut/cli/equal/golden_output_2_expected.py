expected_output = {
    "sessions": {
        "17": {
            "service_policy": {
                "direction": "output",
                "name": "MultiMatchPolicy",
                "class_map": {
                    "class-voice": {
                        "match_type": "match-any",
                        "match": "access-group name VOICE_TRAFFIC"
                    }
                }
            }
        }
    }
}
