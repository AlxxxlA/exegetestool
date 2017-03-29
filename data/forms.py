# coding: utf-8

from django import forms

class ReferenceForm(forms.Form):
    type = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    id = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    authority = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    section = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    title_short = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ECLI = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    URL = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
