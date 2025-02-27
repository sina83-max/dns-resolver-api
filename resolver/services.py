import dns.resolver
import dns.reversename

def resolve_dns(domain, record_type='A'):
    try:
        # Perform dns resolution
        answers = dns.resolver.resolve(domain, record_type)
        # extract records
        records = []
        for r in answers:
            r = str(r)
            records.append(r)
        ttl = answers.rrset.ttl

        return {
            'domain': domain,
            'type': record_type,
            'records': records,
            'ttl': ttl,
        }
    except dns.resolver.NXDOMAIN:
        raise ValueError(f"domain {domain} does not exist")
    except dns.resolver.NoAnswer:
        raise ValueError(f"No {record_type} records exists for '{domain}'")
    except dns.resolver.Timeout:
        raise ValueError("DNS query timed out")


def reverse_dns(ip_address):
    try:
        reverse_name = dns.reversename.from_address(ip_address)
        reversed_dns = dns.resolver.resolve(reverse_name, 'PTR')
        for record in reversed_dns:
            domain_name = []
            record = str(record)
            domain_name.append(record)

        return {
            'ip_address': ip_address,
            'domain_name': domain_name
        }

    except dns.resolver.NXDOMAIN:
       raise ValueError('No domain name associated with this IP address')
    except dns.resolver.Timeout:
        raise ValueError('Reverse DNS query timed out.')
    except dns.resolver.NoNameservers:
        raise ValueError('No nameservers available to handle this request')
    except Exception as e:
        raise ValueError(f'An error occurred: {e}')


