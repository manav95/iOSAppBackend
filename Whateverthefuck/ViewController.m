//
//  ViewController.m
//  Whateverthefuck
//
//  Created by Manav Duttas on 3/21/15.
//  Copyright (c) 2015 Manav Duttas. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController {
}

- (void)viewDidLoad {
    [super viewDidLoad];
    //does stuff
    NSLog(@"this is the stuff: %d", 80);
    NSMutableArray *post = [NSMutableArray arrayWithObjects: @"9", @"15",@"20",@"40",@"70",@"40",@"14",@"43", nil];
    NSMutableDictionary *paste = [NSMutableDictionary new];
    [paste setObject:post forKey:@"data"];
    NSData *jsonData = [NSJSONSerialization dataWithJSONObject:paste options:0 error: nil];
    NSString *jsonString = [[NSString alloc] initWithData:jsonData encoding:NSASCIIStringEncoding];
    NSString *postLength = [NSString stringWithFormat:@"%d",[jsonString length]];
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    [request setURL:[NSURL URLWithString:@"http://127.0.0.1:9875/recordData"]];
    [request setHTTPMethod:@"POST"];
    [request setValue:postLength forHTTPHeaderField:@"Content-Length"];
    [request setHTTPBody:jsonData];
    NSURLResponse *requestResponse;
    NSData *requestHandler = [NSURLConnection sendSynchronousRequest:request returningResponse:&requestResponse error:nil];
    NSString *requestReply = [[NSString alloc] initWithBytes:[requestHandler bytes] length:[requestHandler length] encoding:NSASCIIStringEncoding];
    NSLog(@"requestReply: %@", requestReply);
    // Do any additional setup after loading the view, typically from a nib.
    //does Get stuff
    request = [[NSMutableURLRequest alloc] init];
    [request setURL:[NSURL URLWithString:@"http://127.0.0.1:9875/trainingData"]];
    [request setHTTPMethod:@"GET"];
    NSURLResponse *secResponse;
    requestHandler = [NSURLConnection sendSynchronousRequest:request returningResponse:&secResponse error:nil];
    
    requestReply = [[NSString alloc] initWithBytes:[requestHandler bytes] length:[requestHandler length] encoding:NSASCIIStringEncoding];
    NSLog(@"requestReply: %@", requestReply);
    
    
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
