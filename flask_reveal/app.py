# -*- coding: utf-8 -*-

from flask import Flask

from .blueprints.reveal import reveal_blueprint


class FlaskReveal(Flask):
    """
    Class that extends the Flask class loads the project
    specific configurations
    """

    def __init__(self, import_name, **kwargs):
        super(FlaskReveal, self).__init__(import_name, **kwargs)

        self.config.from_object('flask_reveal.config')
        self.register_blueprint(reveal_blueprint)

    def load_user_config(self, presentation_root, media_root, config=None):
        """
        Loading the user presentation configuration

        :param presentation_root: path to the presentation root
        :param media_root: path to the media root
        """

        self.config['PRESENTATION_ROOT'] = presentation_root
        self.config['MEDIA_ROOT'] = media_root

        if config:
            try:
                self.config.from_pyfile(config)
            except FileNotFoundError:
                raise

    def start(self, presentation_root, media_root, config=None, debug=False):
        """
        Starting method that handles configuration and starts the app

        :param presentation_root: path to the presentation root
        :param media_root: path to the media root
        :param debug: debug flag
        """
        try:
            self.load_user_config(presentation_root, media_root, config)
        except FileNotFoundError:
            raise

        self.run(debug=debug)
