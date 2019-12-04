from .version import __version__

def api_help():
  print('''
Usage: stackd COMMAND [OPTIONS]

STACKD %s - A docker swarm deploy helper according to environment 🦊
see https://gitlab.com/youtopia.earth/ops/stackd/

Commands:
  deploy                        docker stack deploy (alias: up)
  rm                            docker stack rm (alias: remove) (sync)
  getname
  env                           to load env vars in current bash: export $(stackd env)
  ls                            docker stack ls
  ps                            docker stack ps
  infos                         display env files, compose files and vars
  compo                         display yaml compose result (docker compose config --no-interpolate)
  compo-freeze                  display yaml compose result (docker compose config)
  getimagelist                  list all images required by services
  pull                          pull images required by services
  deploy-with-portainer         docker stack deploy using portainer api
  rm-with-portainer             docker stack rm using portainer api
  config-prune                  remove specified config unused versions
  build                         docker-compose build
  bundle                        create a bundle
  logs                          docker service logs
  vc                            remove stack's volumes
  cc                            remove stack's exited containers
  clear                         (before-clear +) rm + vc (+ after-clear)
  reset                         clear + up
  exec                          docker exec with auto-select
  sh                            exec -it sh
  bash                          exec -it bash
  update                        update services if image changed
  upgrade                       pull + update
  reboot-docker                 restart docker daemon with bugfixs
  stacks                        up|rm|logs stacks
  help                          show this page (alias: h)

  ''' % (__version__) )