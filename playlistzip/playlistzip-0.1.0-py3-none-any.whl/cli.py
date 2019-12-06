import re
import argparse
import json
import pycurl
from jsonpath_rw import jsonpath, parse
from io import BytesIO

def combine_episodes(episode_dicts):
    combo = {}
    for ep, v in episode_dicts[0].items():
        matching = [ d[ep][1] if ep in d else None for d in episode_dicts[1:] ]
        if any(matching):
            combo[ep] = ( v[0], [ v[1] ] + matching )
    return combo;

def pick_json_element(body, regex):
    m = regex.search(body)
    return m.group(1)

def get_episode(text, regs):
    m = first_true(map(lambda v:v.search(text), regs), bool)
    return m.group(1) if m else False

def first_true(iterable, pred=None, default=False):
    return next(filter(pred, iterable), default)

def get_episodes(pl_json, compiled_regs):
    fvideo = parse('$..playlistVideoRenderer')
    out_dict = {}
    for m in fvideo.find(pl_json):
        title = m.value['title']['runs'][0]['text']
        vid = m.value['videoId']

        episode = get_episode(title, compiled_regs)
        if episode:
            out_dict[episode] = (title, vid)
    return out_dict

def get_next_token(pl_json):
    ftoken = parse('$..nextContinuationData.continuation')
    found = ftoken.find(pl_json)
    return found[0].value if len(found) > 0 else False

def fetch(url, agent, headers):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.USERAGENT, agent)
    c.setopt(c.HTTPHEADER, headers)
    c.perform()
    c.close()
    return buffer.getvalue()

def collect_eps(eps, token, agent, headers, compiled_regs):
    while bool( token ):
        url = "https://m.youtube.com/playlist?ctoken={}&pbj=1".format(token)
        body = fetch(url, agent, headers)
        njson = json.loads(body)
        token = get_next_token(njson)
        eps.update(get_episodes(njson, compiled_regs))
    return eps

def fetch_ep_id_dict( playlist_id, find_json_regex, compiled_regs ):
    agent = "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    headers = [
            "X-YouTube-Client-Name: 2",
            "X-YouTube-Client-Version: 2.20191115.05.00"
            ]
    url = "https://m.youtube.com/playlist?list={}".format(playlist_id)
    body = fetch(url, agent, headers)
    pl_json = json.loads(pick_json_element(body.decode('utf-8'), find_json_regex))
    eps = get_episodes(pl_json, compiled_regs)
    next_token = get_next_token(pl_json)
    if bool( next_token ):
        eps = collect_eps(eps, next_token, agent, headers, compiled_regs)
    return eps

def compile_regs(first, second, third, fourth):
    default_regs = [ r'Episode ([0-9]{1,2})', r'#([0-9]{1,2})', r'([0-9]{1,2})' ]
    dregs_compiled = [ re.compile(reg) for reg in default_regs ]
    return [
        compile_reg_list(first) if first else dregs_compiled,
        compile_reg_list(second) if second else dregs_compiled,
        compile_reg_list(third) if third else dregs_compiled,
        compile_reg_list(fourth) if fourth else dregs_compiled,
    ]

def compile_reg_list(regs):
    return [ re.compile(r) for r in regs ]

def main():
    parser = argparse.ArgumentParser(description='Description')
    parser.add_argument('playlists', nargs='+')
    parser.add_argument('--first-regex', action='append')
    parser.add_argument('--second-regex', action='append')
    parser.add_argument('--third-regex', action='append')
    parser.add_argument('--fourth-regex', action='append')
    args = parser.parse_args()

    find_json_regex = re.compile(r'initial-data"><!-- (.*?) -->')

    compiled_regs = compile_regs(args.first_regex, args.second_regex, args.third_regex, args.fourth_regex)
    episode_dicts = [ fetch_ep_id_dict(pl, find_json_regex, compiled_regs[i]) for i, pl in enumerate(args.playlists) ]

    csorted = sorted(combine_episodes(episode_dicts).items(), key=lambda v:int(v[0]))
    for k, groupTuple in csorted:
        params = '&t=0&v='.join([vid for vid in groupTuple[1] if vid is not None])
        print(groupTuple[0], "https://viewsync.net/watch?v=" + params)


