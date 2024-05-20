from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder':'Username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder':'Confirm Password'})

class funcform(forms.Form):
    choices = (
        ('configuration','Running Configuration'),
        ('route','Route'),
        ('interfaces','Interfaces'),
        ('vrf','VRF'),
        ('protocols','Protocols')
    )
    router = forms.CharField(label="Router",max_length=50)
    verification = forms.ChoiceField(label="Verification", choices=choices)
    def __init__(self, *args, **kwargs):
        super(funcform, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['router'].widget.attrs.update({'class': 'form-control'})
        self.fields['verification'].widget.attrs.update({'class': 'form-control'})
    
class resform(forms.Form):
    router = forms.CharField(label="Router",max_length=50)
    def __init__(self, *args, **kwargs):
        super(resform, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['router'].widget.attrs.update({'class': 'form-control'})

class setinterfaceform(forms.Form):
    iprouter = forms.CharField(label="iprouter",max_length=50)
    interface = forms.CharField(label="interface",max_length=50)
    description = forms.CharField(label="description",max_length=50) 
    network = forms.CharField(label="network",max_length=50)
    Masque = forms.CharField(label="Masque",max_length=50)
    def __init__(self, *args, **kwargs):
        super(setinterfaceform, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['iprouter'].widget.attrs.update({'class': 'form-control'})
        self.fields['interface'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['network'].widget.attrs.update({'class': 'form-control'})
        self.fields['Masque'].widget.attrs.update({'class': 'form-control'})

class changehostnameform(forms.Form):
    iprouter = forms.CharField(label="iprouter",max_length=50)
    hostname = forms.CharField(label="hostname",max_length=50)
    def __init__(self, *args, **kwargs):
        super(changehostnameform, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['iprouter'].widget.attrs.update({'class': 'form-control'})
        self.fields['hostname'].widget.attrs.update({'class': 'form-control'})

class ospf_form(forms.Form):
    hostip = forms.CharField(label="hostip",max_length=50)
    ospfprocid = forms.CharField(label="ospfprocid",max_length=50)
    network_i = forms.CharField(label="network_i",max_length=50) 
    area_id = forms.CharField(label="area_id",max_length=50)
    def __init__(self, *args, **kwargs):
        super(ospf_form, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['hostip'].widget.attrs.update({'class': 'form-control'})
        self.fields['ospfprocid'].widget.attrs.update({'class': 'form-control'})
        self.fields['network_i'].widget.attrs.update({'class': 'form-control'})
        self.fields['area_id'].widget.attrs.update({'class': 'form-control'})
        

class eigrp_form(forms.Form):
    hostip = forms.CharField(label="hostip",max_length=50)
    eigrpprocid = forms.CharField(label="eigrpprocid",max_length=50)
    network_i = forms.CharField(label="network_i",max_length=50)
    def __init__(self, *args, **kwargs):
        super(eigrp_form, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['hostip'].widget.attrs.update({'class': 'form-control'})
        self.fields['eigrpprocid'].widget.attrs.update({'class': 'form-control'})
        self.fields['network_i'].widget.attrs.update({'class': 'form-control'})


class rip_form(forms.Form):
    hostip = forms.CharField(label="hostip",max_length=50)
    network_i = forms.CharField(label="network_i",max_length=50)
    def __init__(self, *args, **kwargs):
        super(rip_form, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['hostip'].widget.attrs.update({'class': 'form-control'})
        self.fields['network_i'].widget.attrs.update({'class': 'form-control'})

class L3VPNOSPF_form(forms.Form):
    router_ip = forms.CharField(label="hostip",max_length=50)
    VRF_name = forms.CharField(label="ospfprocid",max_length=50)
    OSPF_ID = forms.CharField(label="network_i",max_length=50) 
    network = forms.CharField(label="area_id",max_length=50)
    area = forms.CharField(label="area_id",max_length=50)
    def __init__(self, *args, **kwargs):
        super(L3VPNOSPF_form, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['router_ip'].widget.attrs.update({'class': 'form-control'})
        self.fields['VRF_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['OSPF_ID'].widget.attrs.update({'class': 'form-control'})
        self.fields['network'].widget.attrs.update({'class': 'form-control'})
        self.fields['area'].widget.attrs.update({'class': 'form-control'})

class L3VPNRIP_form(forms.Form):
    router_ip = forms.CharField(label="hostip",max_length=50)
    VRF_name = forms.CharField(label="ospfprocid",max_length=50)
    ADDRESSE_CE_PE = forms.CharField(label="network_i",max_length=50) 
    def __init__(self, *args, **kwargs):
        super(L3VPNRIP_form, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['router_ip'].widget.attrs.update({'class': 'form-control'})
        self.fields['VRF_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['ADDRESSE_CE_PE'].widget.attrs.update({'class': 'form-control'})

class L3VPNEIGRP_form(forms.Form):
    router_ip = forms.CharField(label="hostip",max_length=50)

    def __init__(self, *args, **kwargs):
        super(L3VPNEIGRP_form, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['router_ip'].widget.attrs.update({'class': 'form-control'})


class creationvrf_form(forms.Form):
    hostip = forms.CharField(label="hostip",max_length=50)
    nom_vrf = forms.CharField(label="nom_vrf",max_length=50)
    rd = forms.CharField(label="rd",max_length=50)
    rt = forms.CharField(label="rt",max_length=50)
    interface_pe = forms.CharField(label="interface_pe",max_length=50)
    adresse_ip_pe = forms.CharField(label="adresse_ip_pe",max_length=50)
    masque = forms.CharField(label="masque",max_length=50)
    
    def __init__(self, *args, **kwargs):
        super(creationvrf_form, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['hostip'].widget.attrs.update({'class': 'form-control'})
        self.fields['nom_vrf'].widget.attrs.update({'class': 'form-control'})
        self.fields['rd'].widget.attrs.update({'class': 'form-control'})
        self.fields['rt'].widget.attrs.update({'class': 'form-control'})
        self.fields['interface_pe'].widget.attrs.update({'class': 'form-control'})
        self.fields['adresse_ip_pe'].widget.attrs.update({'class': 'form-control'})
        self.fields['masque'].widget.attrs.update({'class': 'form-control'})

class clientrip_form(forms.Form):
    hostip = forms.CharField(label="hostip",max_length=50)
    vrf = forms.CharField(label="vrf",max_length=50)
    network_i = forms.CharField(label="network_i",max_length=50)

    def __init__(self, *args, **kwargs):
        super(clientrip_form, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['hostip'].widget.attrs.update({'class': 'form-control'})
        self.fields['vrf'].widget.attrs.update({'class': 'form-control'})
        self.fields['network_i'].widget.attrs.update({'class': 'form-control'})


class clientospf_form(forms.Form):
    hostip = forms.CharField(label="hostip",max_length=50)
    vrf = forms.CharField(label="vrf",max_length=50)
    network_i = forms.CharField(label="network_i",max_length=50)
    ospf_id = forms.CharField(label="ospf_id",max_length=50)
    area_id = forms.CharField(label="area_id",max_length=50)

    def __init__(self, *args, **kwargs):
        super(clientospf_form, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['hostip'].widget.attrs.update({'class': 'form-control'})
        self.fields['vrf'].widget.attrs.update({'class': 'form-control'})
        self.fields['network_i'].widget.attrs.update({'class': 'form-control'})
        self.fields['ospf_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['area_id'].widget.attrs.update({'class': 'form-control'})

class clienteigrp_form(forms.Form):
    hostip = forms.CharField(label="hostip",max_length=50)
    vrf = forms.CharField(label="vrf",max_length=50)
    eigrpprocid = forms.CharField(label="eigrpprocid",max_length=50)

    def __init__(self, *args, **kwargs):
        super(clienteigrp_form, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['hostip'].widget.attrs.update({'class': 'form-control'})
        self.fields['vrf'].widget.attrs.update({'class': 'form-control'})
        self.fields['eigrpprocid'].widget.attrs.update({'class': 'form-control'})

class deleteVRF_form(forms.Form):
    hostip = forms.CharField(label="hostip",max_length=50)
    vrf = forms.CharField(label="vrf",max_length=50)
    def __init__(self, *args, **kwargs):
        super(deleteVRF_form, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['hostip'].widget.attrs.update({'class': 'form-control'})
        self.fields['vrf'].widget.attrs.update({'class': 'form-control'})


class deleteRoutage_form(forms.Form):
    hostip = forms.CharField(label="hostip",max_length=50)
    protocol = forms.CharField(label="protocol",max_length=50)
    def __init__(self, *args, **kwargs):
        super(deleteRoutage_form, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['hostip'].widget.attrs.update({'class': 'form-control'})
        self.fields['protocol'].widget.attrs.update({'class': 'form-control'})
