# StackStorm Slack Lite Pack

Send a text message to the given Slack Channel.

## Configuration

Copy the example configuration in [slacklite.yaml.sample]
to `/opt/stackstorm/configs/slacklite.yaml.sample` and edit as required.

It must contain:

* ``token`` - Authentication Token from your Slack App. https://api.slack.com/apps

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

## Actions

* `slacklite.chat.postMessag` - Sends a message to a slack channel.
