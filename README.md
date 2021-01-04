# Ponthon: ENPC's Python Language Server

## About Ponthon

The work of a lifetime.\
Please donate at https://www.paypal.com/paypalme/Ponthon.

## Requirements

You need the following dependencies to make it work:
- docker
- docker-compose
- pipenv

Other dependencies will be automatically installed. For future release, we plan on
removing those dependencies, but for development it's just easier.
We didn't test it on Windows, but it should work the same way.

**Please check that you are in the docker group! It won't work otherwise.**

To check please type `docker run hello-world` (without sudo). If it exits with an error, add yourself to the docker group with `sudo usermod -aG docker yourUsername` 
and reload the system permission (rebooting works).

## Installation

In the root of the project, you'll find a CLI `utils` that will help you to install, run and test the project. Please use 
`python utils.py --help` for further information.
To install the project, run the following commands:
- `python utils.py install`
- `python utils.py init`
- `python utils.py migrate`

## Usage

In this dev version, you have to make sure that the container is running for Ponthon to work.
To do so, you can use `python utils.py run`. \
Once the container is started, you can find extensions for your favourite editor in the `extensions` folder.\
See `extensions/Readme.md` for further instruction.\
`**Trello** :
https://trello.com/b/hZRqQjoj/projet-tdlog

## Licence

Whatever
