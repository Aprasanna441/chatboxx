from channels.generic.websocket import WebsocketConsumer

from channels.exceptions import StopConsumer
#asynctosync makes synchronous functions work with asynchronous
from asgiref.sync import async_to_sync

import json
from .models import Chat,Group

class MySyncConsumer(WebsocketConsumer):
   
    
   
    def connect(self):
        
        self.group_name=self.scope['url_route']['kwargs']['groupkoname']
        self.user=self.scope['user']
        
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,self.channel_name
            )        
        self.accept()
        
        


    def receive(self, text_data=None, bytes_data=None):
        
        data=json.loads(text_data)
        data['username']=self.scope['user'].username
        
        
        message=data['msg']
        username=data['username']
       
        
        
        

        group=Group.objects.get(name=self.group_name)
        chat=Chat(
            content=data['msg'],
            group=group,
            user=self.scope['user'].username
            
        )
        chat.save()
        
        
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,{
            'type':'chat.message',
            'message':message,
            'username':username

            }
        )
    
        
        

        

    def chat_message(self,event):
       
        self.send(text_data=json.dumps(
            {
            'msg':event['message'],
            'username':event['username']

            }
        ))
        
       
   
    def disconnect(self,event):
        print("Websocket disconnected",event)
        print("Channel layer and channel name are",self.channel_layer,self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,self.channel_name
            )
        raise StopConsumer()




class OurSyncConsumer(WebsocketConsumer):
   
    
   
    def connect(self):
        
        self.group_name=self.scope['url_route']['kwargs']['groupkoname']
        self.user=self.scope['user']
        
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,self.channel_name
            )        
        self.accept()
        
        


    def receive(self, text_data=None, bytes_data=None):
        
        data=json.loads(text_data)
        data['username']=self.scope['user'].username
        
        
        message=data['msg']
        username=data['username']
       
        
        
        

        group=Group.objects.get(name=self.group_name)
        chat=Chat(
            content=data['msg'],
            group=group,
            user=self.scope['user'].username
            
        )
        chat.save()
        
        
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,{
            'type':'chat.message',
            'message':message,
            'username':username

            }
        )
    
        
        

        

    def chat_message(self,event):
       
        self.send(text_data=json.dumps(
            {
            'msg':event['message'],
            'username':event['username']

            }
        ))
        
       
   
    def disconnect(self,event):
        print("Websocket disconnected",event)
        print("Channel layer and channel name are",self.channel_layer,self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,self.channel_name
            )
        raise StopConsumer()