from typing import Any, Dict, Iterable, List, Optional, Union

from pynetbox._gen import definitions
from pynetbox.core.api import Api
from pynetbox.core.app import App
from pynetbox.core.endpoint import Endpoint
from pynetbox.core.response import Record, RecordSet

class Wireless_lan_groupsEndpoint(Endpoint):
    def all(self, limit=0, offset=None) -> RecordSet[definitions.WirelessLANGroup]: ...
    def get(
        self,
        id: Optional[str | int] = None,
        name: Optional[str] = None,
        slug: Optional[str] = None,
        description: Optional[str] = None,
        created: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lte: Optional[str] = None,
        last_updated: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        parent_id: Optional[str | int] = None,
        parent: Optional[str] = None,
        id__n: Optional[str] = None,
        id__lte: Optional[str] = None,
        id__lt: Optional[str] = None,
        id__gte: Optional[str] = None,
        id__gt: Optional[str] = None,
        name__n: Optional[str] = None,
        name__ic: Optional[str] = None,
        name__nic: Optional[str] = None,
        name__iew: Optional[str] = None,
        name__niew: Optional[str] = None,
        name__isw: Optional[str] = None,
        name__nisw: Optional[str] = None,
        name__ie: Optional[str] = None,
        name__nie: Optional[str] = None,
        slug__n: Optional[str] = None,
        slug__ic: Optional[str] = None,
        slug__nic: Optional[str] = None,
        slug__iew: Optional[str] = None,
        slug__niew: Optional[str] = None,
        slug__isw: Optional[str] = None,
        slug__nisw: Optional[str] = None,
        slug__ie: Optional[str] = None,
        slug__nie: Optional[str] = None,
        description__n: Optional[str] = None,
        description__ic: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__nisw: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__nie: Optional[str] = None,
        tag__n: Optional[str] = None,
        parent_id__n: Optional[str] = None,
        parent__n: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Optional[definitions.WirelessLANGroup]: ...
    def filter(
        self,
        id: Optional[str | int] = None,
        name: Optional[str] = None,
        slug: Optional[str] = None,
        description: Optional[str] = None,
        created: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lte: Optional[str] = None,
        last_updated: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        parent_id: Optional[str | int] = None,
        parent: Optional[str] = None,
        id__n: Optional[str] = None,
        id__lte: Optional[str] = None,
        id__lt: Optional[str] = None,
        id__gte: Optional[str] = None,
        id__gt: Optional[str] = None,
        name__n: Optional[str] = None,
        name__ic: Optional[str] = None,
        name__nic: Optional[str] = None,
        name__iew: Optional[str] = None,
        name__niew: Optional[str] = None,
        name__isw: Optional[str] = None,
        name__nisw: Optional[str] = None,
        name__ie: Optional[str] = None,
        name__nie: Optional[str] = None,
        slug__n: Optional[str] = None,
        slug__ic: Optional[str] = None,
        slug__nic: Optional[str] = None,
        slug__iew: Optional[str] = None,
        slug__niew: Optional[str] = None,
        slug__isw: Optional[str] = None,
        slug__nisw: Optional[str] = None,
        slug__ie: Optional[str] = None,
        slug__nie: Optional[str] = None,
        description__n: Optional[str] = None,
        description__ic: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__nisw: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__nie: Optional[str] = None,
        tag__n: Optional[str] = None,
        parent_id__n: Optional[str] = None,
        parent__n: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> RecordSet[definitions.WirelessLANGroup]: ...
    def create(
        self,
        id: Optional[str | int] = None,
        name: Optional[str] = None,
        slug: Optional[str] = None,
        description: Optional[str] = None,
        created: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lte: Optional[str] = None,
        last_updated: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        parent_id: Optional[str | int] = None,
        parent: Optional[str] = None,
        id__n: Optional[str] = None,
        id__lte: Optional[str] = None,
        id__lt: Optional[str] = None,
        id__gte: Optional[str] = None,
        id__gt: Optional[str] = None,
        name__n: Optional[str] = None,
        name__ic: Optional[str] = None,
        name__nic: Optional[str] = None,
        name__iew: Optional[str] = None,
        name__niew: Optional[str] = None,
        name__isw: Optional[str] = None,
        name__nisw: Optional[str] = None,
        name__ie: Optional[str] = None,
        name__nie: Optional[str] = None,
        slug__n: Optional[str] = None,
        slug__ic: Optional[str] = None,
        slug__nic: Optional[str] = None,
        slug__iew: Optional[str] = None,
        slug__niew: Optional[str] = None,
        slug__isw: Optional[str] = None,
        slug__nisw: Optional[str] = None,
        slug__ie: Optional[str] = None,
        slug__nie: Optional[str] = None,
        description__n: Optional[str] = None,
        description__ic: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__nisw: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__nie: Optional[str] = None,
        tag__n: Optional[str] = None,
        parent_id__n: Optional[str] = None,
        parent__n: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> definitions.WirelessLANGroup: ...
    def update(
        self, objects: Iterable[definitions.WirelessLANGroup]
    ) -> [definitions.WirelessLANGroup]: ...
    def delete(self, objects: Iterable[definitions.WirelessLANGroup]): ...
    def choices(self) -> dict: ...
    def count(
        self,
        id: Optional[str | int] = None,
        name: Optional[str] = None,
        slug: Optional[str] = None,
        description: Optional[str] = None,
        created: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lte: Optional[str] = None,
        last_updated: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        parent_id: Optional[str | int] = None,
        parent: Optional[str] = None,
        id__n: Optional[str] = None,
        id__lte: Optional[str] = None,
        id__lt: Optional[str] = None,
        id__gte: Optional[str] = None,
        id__gt: Optional[str] = None,
        name__n: Optional[str] = None,
        name__ic: Optional[str] = None,
        name__nic: Optional[str] = None,
        name__iew: Optional[str] = None,
        name__niew: Optional[str] = None,
        name__isw: Optional[str] = None,
        name__nisw: Optional[str] = None,
        name__ie: Optional[str] = None,
        name__nie: Optional[str] = None,
        slug__n: Optional[str] = None,
        slug__ic: Optional[str] = None,
        slug__nic: Optional[str] = None,
        slug__iew: Optional[str] = None,
        slug__niew: Optional[str] = None,
        slug__isw: Optional[str] = None,
        slug__nisw: Optional[str] = None,
        slug__ie: Optional[str] = None,
        slug__nie: Optional[str] = None,
        description__n: Optional[str] = None,
        description__ic: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__nisw: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__nie: Optional[str] = None,
        tag__n: Optional[str] = None,
        parent_id__n: Optional[str] = None,
        parent__n: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> int: ...

class Wireless_lansEndpoint(Endpoint):
    def all(self, limit=0, offset=None) -> RecordSet[definitions.WirelessLAN]: ...
    def get(
        self,
        id: Optional[str | int] = None,
        ssid: Optional[str] = None,
        auth_psk: Optional[str] = None,
        description: Optional[str] = None,
        created: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lte: Optional[str] = None,
        last_updated: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        group_id: Optional[str | int] = None,
        group: Optional[str] = None,
        vlan_id: Optional[str | int] = None,
        auth_type: Optional[str] = None,
        auth_cipher: Optional[str] = None,
        id__n: Optional[str] = None,
        id__lte: Optional[str] = None,
        id__lt: Optional[str] = None,
        id__gte: Optional[str] = None,
        id__gt: Optional[str] = None,
        ssid__n: Optional[str] = None,
        ssid__ic: Optional[str] = None,
        ssid__nic: Optional[str] = None,
        ssid__iew: Optional[str] = None,
        ssid__niew: Optional[str] = None,
        ssid__isw: Optional[str] = None,
        ssid__nisw: Optional[str] = None,
        ssid__ie: Optional[str] = None,
        ssid__nie: Optional[str] = None,
        auth_psk__n: Optional[str] = None,
        auth_psk__ic: Optional[str] = None,
        auth_psk__nic: Optional[str] = None,
        auth_psk__iew: Optional[str] = None,
        auth_psk__niew: Optional[str] = None,
        auth_psk__isw: Optional[str] = None,
        auth_psk__nisw: Optional[str] = None,
        auth_psk__ie: Optional[str] = None,
        auth_psk__nie: Optional[str] = None,
        description__n: Optional[str] = None,
        description__ic: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__nisw: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__nie: Optional[str] = None,
        tag__n: Optional[str] = None,
        group_id__n: Optional[str] = None,
        group__n: Optional[str] = None,
        vlan_id__n: Optional[str] = None,
        auth_type__n: Optional[str] = None,
        auth_cipher__n: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Optional[definitions.WirelessLAN]: ...
    def filter(
        self,
        id: Optional[str | int] = None,
        ssid: Optional[str] = None,
        auth_psk: Optional[str] = None,
        description: Optional[str] = None,
        created: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lte: Optional[str] = None,
        last_updated: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        group_id: Optional[str | int] = None,
        group: Optional[str] = None,
        vlan_id: Optional[str | int] = None,
        auth_type: Optional[str] = None,
        auth_cipher: Optional[str] = None,
        id__n: Optional[str] = None,
        id__lte: Optional[str] = None,
        id__lt: Optional[str] = None,
        id__gte: Optional[str] = None,
        id__gt: Optional[str] = None,
        ssid__n: Optional[str] = None,
        ssid__ic: Optional[str] = None,
        ssid__nic: Optional[str] = None,
        ssid__iew: Optional[str] = None,
        ssid__niew: Optional[str] = None,
        ssid__isw: Optional[str] = None,
        ssid__nisw: Optional[str] = None,
        ssid__ie: Optional[str] = None,
        ssid__nie: Optional[str] = None,
        auth_psk__n: Optional[str] = None,
        auth_psk__ic: Optional[str] = None,
        auth_psk__nic: Optional[str] = None,
        auth_psk__iew: Optional[str] = None,
        auth_psk__niew: Optional[str] = None,
        auth_psk__isw: Optional[str] = None,
        auth_psk__nisw: Optional[str] = None,
        auth_psk__ie: Optional[str] = None,
        auth_psk__nie: Optional[str] = None,
        description__n: Optional[str] = None,
        description__ic: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__nisw: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__nie: Optional[str] = None,
        tag__n: Optional[str] = None,
        group_id__n: Optional[str] = None,
        group__n: Optional[str] = None,
        vlan_id__n: Optional[str] = None,
        auth_type__n: Optional[str] = None,
        auth_cipher__n: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> RecordSet[definitions.WirelessLAN]: ...
    def create(
        self,
        id: Optional[str | int] = None,
        ssid: Optional[str] = None,
        auth_psk: Optional[str] = None,
        description: Optional[str] = None,
        created: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lte: Optional[str] = None,
        last_updated: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        group_id: Optional[str | int] = None,
        group: Optional[str] = None,
        vlan_id: Optional[str | int] = None,
        auth_type: Optional[str] = None,
        auth_cipher: Optional[str] = None,
        id__n: Optional[str] = None,
        id__lte: Optional[str] = None,
        id__lt: Optional[str] = None,
        id__gte: Optional[str] = None,
        id__gt: Optional[str] = None,
        ssid__n: Optional[str] = None,
        ssid__ic: Optional[str] = None,
        ssid__nic: Optional[str] = None,
        ssid__iew: Optional[str] = None,
        ssid__niew: Optional[str] = None,
        ssid__isw: Optional[str] = None,
        ssid__nisw: Optional[str] = None,
        ssid__ie: Optional[str] = None,
        ssid__nie: Optional[str] = None,
        auth_psk__n: Optional[str] = None,
        auth_psk__ic: Optional[str] = None,
        auth_psk__nic: Optional[str] = None,
        auth_psk__iew: Optional[str] = None,
        auth_psk__niew: Optional[str] = None,
        auth_psk__isw: Optional[str] = None,
        auth_psk__nisw: Optional[str] = None,
        auth_psk__ie: Optional[str] = None,
        auth_psk__nie: Optional[str] = None,
        description__n: Optional[str] = None,
        description__ic: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__nisw: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__nie: Optional[str] = None,
        tag__n: Optional[str] = None,
        group_id__n: Optional[str] = None,
        group__n: Optional[str] = None,
        vlan_id__n: Optional[str] = None,
        auth_type__n: Optional[str] = None,
        auth_cipher__n: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> definitions.WirelessLAN: ...
    def update(
        self, objects: Iterable[definitions.WirelessLAN]
    ) -> [definitions.WirelessLAN]: ...
    def delete(self, objects: Iterable[definitions.WirelessLAN]): ...
    def choices(self) -> dict: ...
    def count(
        self,
        id: Optional[str | int] = None,
        ssid: Optional[str] = None,
        auth_psk: Optional[str] = None,
        description: Optional[str] = None,
        created: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lte: Optional[str] = None,
        last_updated: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        group_id: Optional[str | int] = None,
        group: Optional[str] = None,
        vlan_id: Optional[str | int] = None,
        auth_type: Optional[str] = None,
        auth_cipher: Optional[str] = None,
        id__n: Optional[str] = None,
        id__lte: Optional[str] = None,
        id__lt: Optional[str] = None,
        id__gte: Optional[str] = None,
        id__gt: Optional[str] = None,
        ssid__n: Optional[str] = None,
        ssid__ic: Optional[str] = None,
        ssid__nic: Optional[str] = None,
        ssid__iew: Optional[str] = None,
        ssid__niew: Optional[str] = None,
        ssid__isw: Optional[str] = None,
        ssid__nisw: Optional[str] = None,
        ssid__ie: Optional[str] = None,
        ssid__nie: Optional[str] = None,
        auth_psk__n: Optional[str] = None,
        auth_psk__ic: Optional[str] = None,
        auth_psk__nic: Optional[str] = None,
        auth_psk__iew: Optional[str] = None,
        auth_psk__niew: Optional[str] = None,
        auth_psk__isw: Optional[str] = None,
        auth_psk__nisw: Optional[str] = None,
        auth_psk__ie: Optional[str] = None,
        auth_psk__nie: Optional[str] = None,
        description__n: Optional[str] = None,
        description__ic: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__nisw: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__nie: Optional[str] = None,
        tag__n: Optional[str] = None,
        group_id__n: Optional[str] = None,
        group__n: Optional[str] = None,
        vlan_id__n: Optional[str] = None,
        auth_type__n: Optional[str] = None,
        auth_cipher__n: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> int: ...

class Wireless_linksEndpoint(Endpoint):
    def all(self, limit=0, offset=None) -> RecordSet[definitions.WirelessLink]: ...
    def get(
        self,
        id: Optional[str | int] = None,
        ssid: Optional[str] = None,
        auth_psk: Optional[str] = None,
        description: Optional[str] = None,
        created: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lte: Optional[str] = None,
        last_updated: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        interface_a_id: Optional[str | int] = None,
        interface_b_id: Optional[str | int] = None,
        status: Optional[str] = None,
        auth_type: Optional[str] = None,
        auth_cipher: Optional[str] = None,
        id__n: Optional[str] = None,
        id__lte: Optional[str] = None,
        id__lt: Optional[str] = None,
        id__gte: Optional[str] = None,
        id__gt: Optional[str] = None,
        ssid__n: Optional[str] = None,
        ssid__ic: Optional[str] = None,
        ssid__nic: Optional[str] = None,
        ssid__iew: Optional[str] = None,
        ssid__niew: Optional[str] = None,
        ssid__isw: Optional[str] = None,
        ssid__nisw: Optional[str] = None,
        ssid__ie: Optional[str] = None,
        ssid__nie: Optional[str] = None,
        auth_psk__n: Optional[str] = None,
        auth_psk__ic: Optional[str] = None,
        auth_psk__nic: Optional[str] = None,
        auth_psk__iew: Optional[str] = None,
        auth_psk__niew: Optional[str] = None,
        auth_psk__isw: Optional[str] = None,
        auth_psk__nisw: Optional[str] = None,
        auth_psk__ie: Optional[str] = None,
        auth_psk__nie: Optional[str] = None,
        description__n: Optional[str] = None,
        description__ic: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__nisw: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__nie: Optional[str] = None,
        tag__n: Optional[str] = None,
        interface_a_id__n: Optional[str] = None,
        interface_a_id__lte: Optional[str] = None,
        interface_a_id__lt: Optional[str] = None,
        interface_a_id__gte: Optional[str] = None,
        interface_a_id__gt: Optional[str] = None,
        interface_b_id__n: Optional[str] = None,
        interface_b_id__lte: Optional[str] = None,
        interface_b_id__lt: Optional[str] = None,
        interface_b_id__gte: Optional[str] = None,
        interface_b_id__gt: Optional[str] = None,
        status__n: Optional[str] = None,
        auth_type__n: Optional[str] = None,
        auth_cipher__n: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Optional[definitions.WirelessLink]: ...
    def filter(
        self,
        id: Optional[str | int] = None,
        ssid: Optional[str] = None,
        auth_psk: Optional[str] = None,
        description: Optional[str] = None,
        created: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lte: Optional[str] = None,
        last_updated: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        interface_a_id: Optional[str | int] = None,
        interface_b_id: Optional[str | int] = None,
        status: Optional[str] = None,
        auth_type: Optional[str] = None,
        auth_cipher: Optional[str] = None,
        id__n: Optional[str] = None,
        id__lte: Optional[str] = None,
        id__lt: Optional[str] = None,
        id__gte: Optional[str] = None,
        id__gt: Optional[str] = None,
        ssid__n: Optional[str] = None,
        ssid__ic: Optional[str] = None,
        ssid__nic: Optional[str] = None,
        ssid__iew: Optional[str] = None,
        ssid__niew: Optional[str] = None,
        ssid__isw: Optional[str] = None,
        ssid__nisw: Optional[str] = None,
        ssid__ie: Optional[str] = None,
        ssid__nie: Optional[str] = None,
        auth_psk__n: Optional[str] = None,
        auth_psk__ic: Optional[str] = None,
        auth_psk__nic: Optional[str] = None,
        auth_psk__iew: Optional[str] = None,
        auth_psk__niew: Optional[str] = None,
        auth_psk__isw: Optional[str] = None,
        auth_psk__nisw: Optional[str] = None,
        auth_psk__ie: Optional[str] = None,
        auth_psk__nie: Optional[str] = None,
        description__n: Optional[str] = None,
        description__ic: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__nisw: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__nie: Optional[str] = None,
        tag__n: Optional[str] = None,
        interface_a_id__n: Optional[str] = None,
        interface_a_id__lte: Optional[str] = None,
        interface_a_id__lt: Optional[str] = None,
        interface_a_id__gte: Optional[str] = None,
        interface_a_id__gt: Optional[str] = None,
        interface_b_id__n: Optional[str] = None,
        interface_b_id__lte: Optional[str] = None,
        interface_b_id__lt: Optional[str] = None,
        interface_b_id__gte: Optional[str] = None,
        interface_b_id__gt: Optional[str] = None,
        status__n: Optional[str] = None,
        auth_type__n: Optional[str] = None,
        auth_cipher__n: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> RecordSet[definitions.WirelessLink]: ...
    def create(
        self,
        id: Optional[str | int] = None,
        ssid: Optional[str] = None,
        auth_psk: Optional[str] = None,
        description: Optional[str] = None,
        created: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lte: Optional[str] = None,
        last_updated: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        interface_a_id: Optional[str | int] = None,
        interface_b_id: Optional[str | int] = None,
        status: Optional[str] = None,
        auth_type: Optional[str] = None,
        auth_cipher: Optional[str] = None,
        id__n: Optional[str] = None,
        id__lte: Optional[str] = None,
        id__lt: Optional[str] = None,
        id__gte: Optional[str] = None,
        id__gt: Optional[str] = None,
        ssid__n: Optional[str] = None,
        ssid__ic: Optional[str] = None,
        ssid__nic: Optional[str] = None,
        ssid__iew: Optional[str] = None,
        ssid__niew: Optional[str] = None,
        ssid__isw: Optional[str] = None,
        ssid__nisw: Optional[str] = None,
        ssid__ie: Optional[str] = None,
        ssid__nie: Optional[str] = None,
        auth_psk__n: Optional[str] = None,
        auth_psk__ic: Optional[str] = None,
        auth_psk__nic: Optional[str] = None,
        auth_psk__iew: Optional[str] = None,
        auth_psk__niew: Optional[str] = None,
        auth_psk__isw: Optional[str] = None,
        auth_psk__nisw: Optional[str] = None,
        auth_psk__ie: Optional[str] = None,
        auth_psk__nie: Optional[str] = None,
        description__n: Optional[str] = None,
        description__ic: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__nisw: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__nie: Optional[str] = None,
        tag__n: Optional[str] = None,
        interface_a_id__n: Optional[str] = None,
        interface_a_id__lte: Optional[str] = None,
        interface_a_id__lt: Optional[str] = None,
        interface_a_id__gte: Optional[str] = None,
        interface_a_id__gt: Optional[str] = None,
        interface_b_id__n: Optional[str] = None,
        interface_b_id__lte: Optional[str] = None,
        interface_b_id__lt: Optional[str] = None,
        interface_b_id__gte: Optional[str] = None,
        interface_b_id__gt: Optional[str] = None,
        status__n: Optional[str] = None,
        auth_type__n: Optional[str] = None,
        auth_cipher__n: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> definitions.WirelessLink: ...
    def update(
        self, objects: Iterable[definitions.WirelessLink]
    ) -> [definitions.WirelessLink]: ...
    def delete(self, objects: Iterable[definitions.WirelessLink]): ...
    def choices(self) -> dict: ...
    def count(
        self,
        id: Optional[str | int] = None,
        ssid: Optional[str] = None,
        auth_psk: Optional[str] = None,
        description: Optional[str] = None,
        created: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lte: Optional[str] = None,
        last_updated: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        interface_a_id: Optional[str | int] = None,
        interface_b_id: Optional[str | int] = None,
        status: Optional[str] = None,
        auth_type: Optional[str] = None,
        auth_cipher: Optional[str] = None,
        id__n: Optional[str] = None,
        id__lte: Optional[str] = None,
        id__lt: Optional[str] = None,
        id__gte: Optional[str] = None,
        id__gt: Optional[str] = None,
        ssid__n: Optional[str] = None,
        ssid__ic: Optional[str] = None,
        ssid__nic: Optional[str] = None,
        ssid__iew: Optional[str] = None,
        ssid__niew: Optional[str] = None,
        ssid__isw: Optional[str] = None,
        ssid__nisw: Optional[str] = None,
        ssid__ie: Optional[str] = None,
        ssid__nie: Optional[str] = None,
        auth_psk__n: Optional[str] = None,
        auth_psk__ic: Optional[str] = None,
        auth_psk__nic: Optional[str] = None,
        auth_psk__iew: Optional[str] = None,
        auth_psk__niew: Optional[str] = None,
        auth_psk__isw: Optional[str] = None,
        auth_psk__nisw: Optional[str] = None,
        auth_psk__ie: Optional[str] = None,
        auth_psk__nie: Optional[str] = None,
        description__n: Optional[str] = None,
        description__ic: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__nisw: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__nie: Optional[str] = None,
        tag__n: Optional[str] = None,
        interface_a_id__n: Optional[str] = None,
        interface_a_id__lte: Optional[str] = None,
        interface_a_id__lt: Optional[str] = None,
        interface_a_id__gte: Optional[str] = None,
        interface_a_id__gt: Optional[str] = None,
        interface_b_id__n: Optional[str] = None,
        interface_b_id__lte: Optional[str] = None,
        interface_b_id__lt: Optional[str] = None,
        interface_b_id__gte: Optional[str] = None,
        interface_b_id__gt: Optional[str] = None,
        status__n: Optional[str] = None,
        auth_type__n: Optional[str] = None,
        auth_cipher__n: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> int: ...

class WirelessApp(App):
    def __init__(self, api: "Api", name):
        self.wireless_lan_groups: Wireless_lan_groupsEndpoint = ...
        self.wireless_lans: Wireless_lansEndpoint = ...
        self.wireless_links: Wireless_linksEndpoint = ...
