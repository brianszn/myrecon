from src.cli import interface
from src.core import port_scan, scraping
from src.core.hackertarget import hostsearch, iplookup
from src.core import user_agent
import argparse


if __name__ == '__main__':

    print(interface.banner())

    parser = argparse.ArgumentParser(prog='my-recon')
    parser.add_argument('--url', help='URL', required=True)
    parser.add_argument('--full', help='Full recon', action='store_true')
    parser.add_argument('--hostsearch', help='......', action='store_true')
    parser.add_argument('--iplookup', help='......', action='store_true')
    parser.add_argument('--portscan', help='......', action='store_true')
    args = parser.parse_args()
    url = args.url

    
    if args.full:

        print('...')

    elif args.hostsearch:

        hostsearch.hostsearch(url)

    elif args.iplookup:

        print('...')

    elif args.portscan:
        print('...')
    
    else:

        print('...')
        

        


        
       

    
 
        
    
    

    












