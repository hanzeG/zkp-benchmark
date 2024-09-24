import { useState } from 'react'
import Image from 'next/image'
import NextLink from 'next/link'
import {
  TableContainer, Box, Table, Thead, Tbody, Th, Tr, Td, Stack, HStack, Text, Button, IconButton,
  Popover, PopoverTrigger, PopoverContent, PopoverArrow, Portal, PopoverBody, Icon, Spacer, Link,
  useColorModeValue, Tooltip,
} from '@chakra-ui/react'
import { WarningIcon, InfoIcon } from '@chakra-ui/icons'
// import { MdInfo } from 'react-icons/md'
import { FaExternalLinkAlt } from 'react-icons/fa'
import { frameworks } from '@/fixtures/frameworks'
import benchmarks from '@/fixtures/benchmarks.json'
import bytes from 'bytes'
import { timeSinceLastUpdate } from '@/util/date'

const machines = [{
  name: 'AWS m5.xLarge',
  prop: 'm5_xLarge',
  // Cost per hour
  cost: 1.008,
}, {
  name: 'AWS m5.4xlarge',
  prop: 'm5_4xlarge',
  // Cost per hour
  cost: 4.032,
}, {
  name: 'AWS m5.12xlarge',
  prop: 'AWS m5.12xlarge',
  // Cost per hour
  cost: 4.032,
}, {
  name: 'AWS m6g.12xlarge',
  prop: 'AWS m6g.12xlarge',
  // Cost per hour
  cost: 1.008,
}, {
  name: 'AWS r6i.12xlarge',
  prop: 'AWS r6i.12xlarge',
  // Cost per hour
  cost: 4.032,
}, {
  name: 'AWS c6i.12xlarge',
  prop: 'AWS c6i.12xlarge',
  // Cost per hour
  cost: 4.032,
}]

const hashType = [{
  id: 'type1',
  name: 'Low-degree',
  prop: 'Low-degree',
}, {
  id: 'type2',
  name: 'Low-degree Equivalence',
  prop: 'Low-degree Equivalence',
}, {
  id: 'type3',
  name: 'Lookup Tables',
  prop: 'Lookup Tables',
}, {
  id: 'type0',
  name: 'Non-optimized',
  prop: 'Non-optimized',
}]

const metrics = [{
  id: 'time',
  name: 'Time',
  prop: 'time',
}, {
  id: 'memory',
  name: 'Memory',
  prop: 'metrics.memory_usage_bytes',
}, {
  id: 'proof_size',
  name: 'Proof Size',
  prop: 'metrics.proof_size_bytes',
}, {
  id: 'cost',
  name: 'Cost',
  prop: 'time',
}]

interface ResultTableProperty {
  name: string;
  desc?: string | JSX.Element;
  hash?: string | Array<string>;
  prop?: string;
  indent?: number;
  annotations?: Record<string, string | JSX.Element>
  value?: (val: any, vars: Record<string, any>) => any;
}

const metricFormatter = (empty = '') => (val: any, vars: Record<string, any>) => {
  if (!val) return empty
  if (vars.cost) {
    const machineCost = machines.find((m) => m.prop === vars.machine)?.cost
    if (!machineCost) return empty
    const machinePerSecond = machineCost / 60 / 60
    return `$${formatToTwoSignificantDigits((val.secs + val?.nanos / 1000000000) * machinePerSecond)}`
  }
  if (vars.metric == 'time') {
    return `${(val.secs + val?.nanos / 1000000000).toFixed(2)}s`
  }
  return bytes(val)
}

const MoreInfo = ({ children, count, more }: any) => (
  <HStack><Text>{children}</Text><Tooltip label={more}><Text color='blue.700' cursor='pointer'>+{count} more</Text></Tooltip></HStack>
)

const properties: ResultTableProperty[] = [{
  name: 'Frontend (Language)',
  prop: 'frontend',
  desc: 'Frontend is the technical term for a programming language that is compiled into a lower level language',
}, {
  name: 'ZK',
  prop: 'zk',
  desc: 'The type of ZK used, for a detailed comparison, see the FAQ section below.',
},
{
  name: 'Assert',
  desc: 'A very simple assertion a != b, this can be used to test the framework\'s minimum proving performance.',
  prop: 'metrics.$machine.assert.results.0.$metric',
  value: metricFormatter(),
  annotations: {
    risc_zero: 'Risc Zero is significantly slower for this test, as the minimum number of cycles for all Risc Zero programs is 64k. Therefore this very small program still requires a large number of cycles.',
  },
}, {
  name: 'ZK-Friendly Hashes', hash: ['type1', 'type2', 'type3'],
  prop: 'zkHash',
  desc: 'Hashes that have been optimised by the framework and therefore should perform faster. SHA-256 and Blake are not optimised for ZK in general, but may still be optimised by a framework.',
  value: (val) => val.length > 1 ? <MoreInfo count={val.length - 1} more={val.slice(1).join(', ')}>{val[0]}</MoreInfo> : val?.[0],
  annotations: {
    risc_zero: 'SHA-256 is the most optimised hash for Risc Zero, but SHA-256 is in general not ZK optimised.',
  },
}, {
  name: 'Non-optimized Hashes', hash: 'type0',
  prop: 'hash',
  desc: 'Hashes are not optimised for ZK in general, but may still be optimized by a framework.',
  value: (val) => val.length > 1 ? <MoreInfo count={val.length - 1} more={val.slice(1).join(', ')}>{val[0]}</MoreInfo> : val?.[0],
},
// type 0 hash functions

{
  name: 'SHA-256', hash: 'type0',
  indent: 4,
  desc: 'Calculating the SHA-256 hash for given input size. SHA-256 is NOT zk optimised so it\'s normal to see degraded performance compared to other hashes. You SHOULD use an alterantive ZK-optimised hash if your use case allows and the framework provides it.',
  prop: 'metrics.$machine.Fibonacci.results.0.$metric',
  value: metricFormatter(),
  annotations: {
    leo: 'We used SHA3, as no SHA2 was available',
  },
},

// blake
{
  name: 'Blake2', hash: 'type0',
  indent: 4,
  desc: 'Calculating the Blake hash for given input size. Blake is NOT zk optimised so it\'s normal to see degraded performance compared to other hashes. You SHOULD use an alterantive ZK-optimised hash if your use case allows and the framework provides it.',
  prop: 'metrics.$machine.Fibonacci.results.0.$metric',
  value: metricFormatter(),
  annotations: {
    leo: 'We used SHA3, as no SHA2 was available',
  },
},

// type 1 hash functions

// MiMC
{
  name: 'MiMC', hash: 'type1',
  indent: 4,
  desc: 'A ZK optimised hash, this should perform better than SHA-256.',
  prop: 'metrics.$machine.Fibonacci.results.0.$metric',
  value: metricFormatter(),
  annotations: {
    risc_zero: 'Risc Zero does not support RPO',
    noir: 'Noir does not support RPO, but does support Pederson which is a ZK optimised hash.',
  },
},

// GMiMC
{
  name: 'GMiMC', hash: 'type1',
  indent: 4,
  desc: 'A ZK optimised hash, this should perform better than SHA-256.',
  prop: 'metrics.$machine.Fibonacci.results.0.$metric',
  value: metricFormatter(),
  annotations: {
    risc_zero: 'Risc Zero does not support RPO',
    noir: 'Noir does not support RPO, but does support Pederson which is a ZK optimised hash.',
  },
},

// Neptune
{
  name: 'Neptune', hash: 'type1',
  indent: 4,
  desc: 'A ZK optimised hash, this should perform better than SHA-256.',
  prop: 'metrics.$machine.Fibonacci.results.0.$metric',
  value: metricFormatter(),
  annotations: {
    risc_zero: 'Risc Zero does not support Pedersen',
    polylang: 'Miden does not support Pedersen',
    miden: 'Miden does not support Pedersen',
  },
},

// Poseidon
{
  name: 'Poseidon', hash: 'type1',
  indent: 4,
  desc: 'A ZK optimised hash, this should perform better than SHA-256.',
  prop: 'metrics.$machine.Fibonacci.results.0.$metric',
  value: metricFormatter(),
  annotations: {
    risc_zero: 'Risc Zero does not support Pedersen',
    polylang: 'Miden does not support Pedersen',
    miden: 'Miden does not support Pedersen',
  },
},

// Poseidon2
{
  name: 'Poseidon2', hash: 'type1',
  indent: 4,
  desc: 'A ZK optimised hash, this should perform better than SHA-256.',
  prop: 'metrics.$machine.Fibonacci.results.0.$metric',
  value: metricFormatter(),
  annotations: {
    risc_zero: 'Risc Zero does not support Pedersen',
    polylang: 'Miden does not support Pedersen',
    miden: 'Miden does not support Pedersen',
  },
},

// type 2
// rescue
{
  name: 'Rescue', hash: 'type2',
  indent: 4,
  desc: 'A ZK optimised hash, this should perform better than SHA-256.',
  prop: 'metrics.$machine.Fibonacci.results.0.$metric',
  value: metricFormatter(),
  annotations: {
    risc_zero: 'Risc Zero does not support Pedersen',
    polylang: 'Miden does not support Pedersen',
    miden: 'Miden does not support Pedersen',
  },
},

// Griffin
{
  name: 'Griffin', hash: 'type2',
  indent: 4,
  desc: 'A ZK optimised hash, this should perform better than SHA-256.',
  prop: 'metrics.$machine.Fibonacci.results.0.$metric',
  value: metricFormatter(),
  annotations: {
    risc_zero: 'Risc Zero does not support Pedersen',
    polylang: 'Miden does not support Pedersen',
    miden: 'Miden does not support Pedersen',
  },
},

// anemoi
{
  name: 'Anemoi', hash: 'type2',
  indent: 4,
  desc: 'A ZK optimised hash, this should perform better than SHA-256.',
  prop: 'metrics.$machine.Fibonacci.results.0.$metric',
  value: metricFormatter(),
  annotations: {
    risc_zero: 'Risc Zero does not support Pedersen',
    polylang: 'Miden does not support Pedersen',
    miden: 'Miden does not support Pedersen',
  },
},

// type 3

// tip5
{
  name: 'Tip5', hash: 'type3',
  indent: 4,
  desc: 'A ZK optimised hash, this should perform better than SHA-256.',
  prop: 'metrics.$machine.Fibonacci.results.0.$metric',
  value: metricFormatter(),
  annotations: {
    risc_zero: 'Risc Zero does not support Pedersen',
    polylang: 'Miden does not support Pedersen',
    miden: 'Miden does not support Pedersen',
  },
},

// RC
{
  name: 'Reinforced Concrete', hash: 'type3',
  indent: 4,
  desc: 'A ZK optimised hash, this should perform better than SHA-256.',
  prop: 'metrics.$machine.Fibonacci.results.0.$metric',
  value: metricFormatter(),
  annotations: {
    risc_zero: 'Risc Zero does not support Pedersen',
    polylang: 'Miden does not support Pedersen',
    miden: 'Miden does not support Pedersen',
  },
},

// Monolith
{
  name: 'Monolith', hash: 'type3',
  indent: 4,
  desc: 'A ZK optimised hash, this should perform better than SHA-256.',
  prop: 'metrics.$machine.Fibonacci.results.0.$metric',
  value: metricFormatter(),
  annotations: {
    risc_zero: 'Risc Zero does not support Pedersen',
    polylang: 'Miden does not support Pedersen',
    miden: 'Miden does not support Pedersen',
  },
},

// merkle tree

{
  name: 'Full Binary Merkle Tree',
}, {
  name: '2^10',
  indent: 4,
  prop: 'metrics.$machine.Merkle Membership.results.0.$metric',
  value: metricFormatter('🚧'),
}, {
  name: '2^20',
  indent: 4,
  prop: 'metrics.$machine.Merkle Membership.results.0.$metric',
  value: metricFormatter('🚧'),
}]


export function ResultsTable() {
  const colorMode = useColorModeValue('light', 'dark')
  const [machine, setMachine] = useState(machines[0].prop)
  const [hash, setHashType] = useState(hashType[0].id)
  const [metric, setMetric] = useState(metrics[0].id)
  const vars = {
    machine,
    hash: hashType.find((a) => a.id === hash)?.prop,
    metric: metrics.find((a) => a.id === metric)?.prop,
    cost: metric === 'cost',
  }

  return (
    <Stack fontSize='sm' spacing={4}>
      <Stack>
        <HStack>
          <Text fontWeight='bold'>Hardware:</Text>
          {machines.map(({ name, prop }) => {
            const selected = machine === prop
            return (
              <Button size='sm' variant={selected ? 'solid' : 'ghost'} key={prop} onClick={() => {
                setMachine(prop)
              }}>{name}</Button>
            )
          })}
          <Popover trigger='hover' placement='top'>
            <PopoverTrigger>
              <Button size='sm' opacity='0.4' variant='ghost'>CUDA</Button>
            </PopoverTrigger>
            <PopoverContent>
              <PopoverArrow />
              <PopoverBody><Text overflowWrap='anywhere' fontSize='sm'>Follow on Twitter <Link as={NextLink} color='blue.600' href='https://twitter.com/intent/user?screen_name=polybase_xyz'>@polybase_xyz </Link>to be notified when we add this</Text></PopoverBody>
            </PopoverContent>
          </Popover>
        </HStack>
        <HStack>
          <Text fontWeight='bold'>Hash Functions:</Text>
          {hashType.map(({ name, id }) => {
            const selected = hash === id
            return (
              <Button size='sm' variant={selected ? 'solid' : 'ghost'} key={id} onClick={() => {
                setHashType(id)
              }}>{name}</Button>
            )
          })}
        </HStack>
        <HStack>
          <Text fontWeight='bold'>Metrics:</Text>
          {metrics.map(({ name, id }) => {
            const selected = metric === id
            return (
              <Button size='sm' variant={selected ? 'solid' : 'ghost'} key={id} onClick={() => {
                setMetric(id)
              }}>{name}</Button>
            )
          })}
        </HStack>
      </Stack>
      <Box border='1px solid' borderBottomWidth={0} borderColor='bw.100' borderRadius={5}>
        <TableContainer overflowX='unset' overflowY='unset'>
          <Table>
            <Thead>
              <Tr>
                <Th position='sticky' top={0} background='bws' zIndex={1000}>
                </Th>
                {frameworks.map((item) => (
                  <Th key={item.name} fontSize='sm' position='sticky' top={0} background='bws' zIndex={1000}>
                    <a href={item.url} target='_blank'>
                      <Stack spacing={2}>
                        <Box textDecorationColor='#fff'>
                          <Image
                            alt={item.name}
                            src={item.logo.src[colorMode]}
                            height={item.logo.height}
                            width={item.logo.width}
                          />
                        </Box>
                        <Box>{item.name} <Icon opacity='0.4' fontSize='xs' as={FaExternalLinkAlt} /></Box>
                      </Stack>
                    </a>
                  </Th>
                ))}
              </Tr>
            </Thead>
            <Tbody>
              {properties
                .filter(prop => !prop.hash || (Array.isArray(prop.hash) ? prop.hash.includes(hash) : prop.hash === hash))
                .map(prop => {
                  return (
                    <Tr key={prop.name}>
                      <Td fontWeight='600'>
                        <HStack pl={prop.indent ?? 0} spacing={1}>
                          <Box>
                            {prop.name}
                          </Box>

                          {prop.desc && (
                            <Box>
                              <Popover>
                                <PopoverTrigger>
                                  <IconButton opacity={0.3} variant='ghost' aria-label='info' height='18px' size='sm' icon={<InfoIcon />} />
                                </PopoverTrigger>
                                <Portal>
                                  <PopoverContent>
                                    <PopoverArrow />
                                    <PopoverBody><Text overflowWrap='anywhere' fontSize='sm'>{prop.desc}</Text></PopoverBody>
                                  </PopoverContent>
                                </Portal>
                              </Popover>
                            </Box>
                          )}
                        </HStack>
                      </Td>
                      {
                        frameworks.map((fw: any) => {
                          let value = prop.value ? prop.value(getPathValue(fw, prop.prop, vars), vars) : getPathValue(fw, prop.prop, vars)
                          const annotation = prop.annotations?.[fw.id]
                          return (
                            <Td key={fw.name}>
                              <HStack spacing={1}>
                                <Box>
                                  {value}
                                </Box>
                                {annotation && (
                                  <Box>
                                    <Popover>
                                      <PopoverTrigger>
                                        <IconButton variant='ghost' height='18px' aria-label='info' size='sm' icon={<WarningIcon color='orange.400' />} />
                                      </PopoverTrigger>
                                      <Portal>
                                        <PopoverContent>
                                          <PopoverArrow />
                                          <PopoverBody><Text overflowWrap='anywhere' fontSize='sm'>{annotation}</Text></PopoverBody>
                                        </PopoverContent>
                                      </Portal>
                                    </Popover>
                                  </Box>
                                )}
                              </HStack>
                            </Td>
                          )
                        })
                      }
                    </Tr>
                  )
                })}
            </Tbody>
          </Table>
        </TableContainer>
      </Box>
      <Box px={2}>
        <HStack spacing={1} fontStyle='italic'>
          <Text fontWeight={600}>
            Last Updated:
          </Text>
          <Box>
            {timeSinceLastUpdate(benchmarks.meta.lastUpdated)} (<time>{benchmarks.meta.lastUpdated}</time>)
          </Box>
        </HStack>
      </Box>
    </Stack >
  )
}


function getPathValue(data: any, path?: string, vars?: Record<string, any>) {
  if (!path) return
  let current = data
  for (let part of path.split('.')) {
    if (!current) return undefined
    if (part.startsWith('$')) {
      part = vars?.[part.slice(1)]
      if (part.split('.').length > 1) {
        for (let sub of part.split('.')) {
          current = current[sub]
        }
        continue
      }
    }
    current = current[part]
  }
  return current
}

function formatToTwoSignificantDigits(num: number): string {
  if (num === 0) {
    return '0.00'
  }

  const magnitude = Math.floor(Math.log10(Math.abs(num)))
  const power = 1 - magnitude
  const roundedNumber = Math.round(num * Math.pow(10, power)) * Math.pow(10, -power)

  // When the number is less than 1
  if (magnitude < 0) {
    const placesAfterDecimal = Math.abs(magnitude) + 1
    return roundedNumber.toFixed(placesAfterDecimal)
  } else {
    const factor = Math.pow(10, magnitude - 1)
    return (roundedNumber * factor).toFixed(Math.max(0, magnitude - 1))
  }
}